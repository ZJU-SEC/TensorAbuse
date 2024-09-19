# TensorAbuse

This is a TenserAbuse toolkit, which includes tools for analyzing TensorFlow APIs and detecting malicious models.

* PersistExt (Persistent API extraction): This is a tool for analyzing TensorFlow source code. It extracts persistent APIs, corresponding op names, and function source code, allowing further capability analysis by LLMs (Large Language Models).
* CapAnalysis (Capability analysis): This is a tool that leverages LLMs to analyze API capabilities. It constructs prompts using a chain-of-thought approach and supports few-shot prompting for analysis. The process involves two rounds of querying the LLM.
* TensorDetect (TensorAbuse attack detection): This tool is designed to detect malicious TensorFlow models. Currently, it can identify attacks embedded within Lambda layers and TensorAbuse-type exploits.

To use toolkit, you need download the source code and install dependencies first.

```shell
git clone https://github.com/unsatisfying/TensorAbuse.git
pip install -r requirements.txt
```

# PersistExt (Persistent API extraction)

PersistExt takes advantage of TensorFlow’s design for cross-language invocation. At the higher level, it provides Python APIs for developers to build models (e.g., `tf.add`, `tf.nn.softmax`). TensorFlow compiles the model built from these APIs into a graph structure. The TensorFlow graph consists of nodes and edges—where nodes represent TensorFlow’s built-in ops, and edges represent the flow of tensors between these nodes. When a user runs the model, each op is executed, and TensorFlow looks up the corresponding op kernel implementation in the C++ backend’s op registry to invoke it.

PersistExt leverages this cross-language interaction by analyzing the function’s AST (Abstract Syntax Tree) to extract the cross-language invocation interfaces for TensorFlow API extraction. Specifically, it identifies Python-side APIs using the following characteristics:

* Files in the TensorFlow source code ending with .py (often named like `gen_xxx.py`)
* Functions that call fast execution interfaces (e.g., `pywrap_tfe.TFE_Py_FastPathExecute` or `_pywrap_tensorflow.TFE_Py_FastPathExecute`)
* Functions that call apply_op-related interfaces (e.g., `_op_def_lib.apply_op`, `_op_def_lib._apply_op_helper`, or `_op_def_library._apply_op_helper`)

## Usage

First, use pip to download the precompiled source code, or manually compile it according to the [documentation](https://www.tensorflow.org/install/source). This is because most Python files containing ops (like `gen_xxx.py`) are generated after the source code is compiled.

```shell
# tensorflow==2.15.0: can use other versions(e.g.tensorflow==1.0.0)
# -t ./tf_src: Installation path for the source code.
# --no-deps: No dependency packages are needed.

# --python-version 3.10 --ignore-requires-python: Ignore specific Python version requirements and install packages for a particular Python version. This is mainly because some older TensorFlow versions don't support higher Python versions. 
# Since the Windows package may not include the source code, you need to download the Linux package for analysis. Add the `--platform` parameter for this.
$ pip install tensorflow==2.15.0 -t ./tf_src --no-deps --python-version 3.10 --ignore-requires-python
```

Then, invoke **PersistExt** to parse the Python APIs.

```shell
# -p: The TensorFlow source code folder that needs to be parsed.
# -v: TensorFlow version, must be semantic version (ie a.b.c)
# -t: The file path to store result
$ python main.py -p ./tf_src -v 2.15.0 -t result.json
```

Next, users need to follow the official [CodeQL documentation](https://docs.github.com/en/code-security/codeql-for-vs-code) and [VSCode tutorials](https://marketplace.visualstudio.com/items?itemName=github.vscode-codeql#checking-access-to-the-codeql-cli) to install [CodeQL](https://codeql.github.com/) and configure the relevant [VSCode extensions](https://marketplace.visualstudio.com/items?itemName=github.vscode-codeql#checking-access-to-the-codeql-cli). Secondly, in order to compile TensorFlow source code, users need to install the corresponding version of [bazel](https://bazel.build/) (if it is TensorFlow 2.15.0, bazel=6.1.0).

Before parsing the C++ side code, we need to compile TensorFlow source code to generate a database for CodeQL query.

```shell
$ cd tf_src
$ codeql database create new-tensorflow-database --language=cpp --command='path/to/TensorAbuse/PersistExt/codeQL/script/build.sh'
```

Then, we follow [CodeQL query tutorial](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries) and select `new-tensorflow-database` as target database. After that, we invoke **extract_x.ql** to parse the C++ side code, marcos and extract all op kernels implementations.

> Tips: If users have no idea how to run `.ql` file, please refer to [vscode-codeql-starter](https://github.com/github/vscode-codeql-starter). Users can directly use the configuration in the `codeql-custom-queries-cpp` folder and replace the `example.ql` file with the `.ql` files in `TensorAbuse/PersisExt/codeQL/query` to successfully run the query of the .ql files.

## Analysis

In the `analysis` folder, we analyze the previously extracted Python interface code, C++ macro, and C++ OpKernel code to build a complete **Python - C++** cross-language call chain.

```shell
$ cd PersistExt/analysis
$ python analysis.py
```

Before running `analysis.py`, users need to replace `/path/to/TensorFlow_source_code` with their own path to TensorFlow source code folder.

`analysis.py` will extract the python interface code from the excel folder, as well as the location of the C++ code obtained by codeQL analysis in the TensorFlow source code folder. After that, `analysis.py` will extract the C++ code, C++ macros, etc., and build a complete set of **python - C++** cross-language call chains together with the previously obtained python interface code, and save them in a newly generated JSON file.

## Result

We have pre-analyzed APIs for some TensorFlow versions in the [`PersistExt/results` directory](PersistExt/results). Each line represents the function name, OP name, and the relative file path where the API is located. Additionally, [`PersistExt/API_tf_version_analysis.ipynb` file](PersistExt/API_tf_version_analysis.ipynb) contains information on the presence of ops across different TensorFlow versions.

# CapAnalysis (Capability analysis)

**Capanalysis** combines the Python frontend code and C++ backend implementation code of the API into a JSON format and sends it to ChatGPT for querying.

It divides the query into two rounds. The first round roughly categorizes functionality into 5 major types:

* File access
* Network access
* Process management
* Pure calculation
* Code execution

The second round refines these five categories into 13 subcategories based on the results from the first round:

* File access (file read, file write, directory read, directory write)
* Network access (network send, network receive)
* Process management (process create, abort, sleep)
* Pure calculation (mathematical calculation, internal data management, encoding & decoding)
* Code execution (user-controlled function execution)

This refinement helps achieve more accurate results.
Additionally, due to inherent limitations of LLMs, the analysis results are not guaranteed to be 100% accurate. Experimental results show an accuracy of around 83%, but repeating queries with the LLM can increase the accuracy to over 90%.

## Usage

For CapAnalysis, we provide a function interface for use. Users need to combine the previously analyzed Python frontend code and C++ backend code into a JSON file, then call the function directly in Python (user may need their own OpenAI key and modify the [source code file](CapAnalysis/op_analysis_round2.py)).

```Python
# in CapAnalysis/op_analysis_round2.py or 
# CapAnalysis/op_analysis_round1.py file
openai.api_key = "USE_YOUR_API"  
```

Here is a sample demo.py code:

```Python
from CapAnalysis import op_analysis_round2

# JSON format to be queried containing combined Python and C++ code
query_json = 
{
    "Python_codes": <python_code>, 
    "Cpp_codes": <cpp_code>
}
# Call the CapAnalysis function
result = op_analysis_round2.analyze_code_with_chatgpt(query_json)

# Print the result
print(result)

```

## Result

The [`tf_v2.15_result.json` file](CapAnalysis/results/tf_v2.15_result.json) contains the analysis results for TensorFlow 2.15 APIs. Each record includes:

- **op_name**: The name of the op
- **python_code**: The Python frontend code
- **cpp_code**: The C++ backend code
- **round1_result**: The result from the first round of querying ChatGPT
- **round2_result**: The result from the second round of querying ChatGPT

# TensorDetect (TensorAbuse attack detection)

**TensorDetect** is a tool for detecting malicious behavior in TensorFlow models. Currently, it supports detecting Lambda layers and TensorAbuse attacks. It can analyze TensorFlow models in both H5 and SavedModel formats.

For H5 models, **TensorDetect** checks `.h5` files for embedded Lambda layers. If Lambda layers are found, it issues a meddile-severity warning and outputs the information about the Lambda layers.

For SavedModel models, **TensorDetect** inspects zip archives or extracted folders. It extracts the `saved_model.pb` file and analyzes it for suspicious ops. If any ops have parameters indicating malicious files or IPs, it issues a high-severity warning. Otherwise, it issues a medium-severity warning and provides the parameter information.
**TensorDetect** also inspects lambda layer for SavedModel models.

## Usage

Use the following command to invoke the tool:

```shell
$ python main.py -m TensorDetect/demo_models/tensorabuse_savedmodel
```
