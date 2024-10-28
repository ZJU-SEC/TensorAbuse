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

First, download TensorFlow 2.15.0 source code zip file, and manually compile it according to the [documentation](https://www.tensorflow.org/install/source). We need to compile TensorFlow from source code because most Python files containing ops (like `gen_xxx.py`) are generated after the source code is compiled, and we need those C++ side code for PersistExt analysis.

In order to compile TensorFlow source code, users need to install the corresponding version of [bazel](https://bazel.build/) (if it is TensorFlow 2.15.0, bazel=6.1.0).

```shell
#!/bin/bash
$ URL="https://sourceforge.net/projects/tensorflow.mirror/files/v2.15.0/TensorFlow%202.15.0%20source%20code.zip/download"
$ FILENAME="tensorflow-2.15.0.zip"
$ TARGET_DIR="tf_src"

$ wget -O $FILENAME $URL
$ mkdir -p $TARGET_DIR
$ unzip $FILENAME -d $TARGET_DIR

$ cd tf_src/tensorflow-tensorflow-6887368
$ bazel clean --expunge
$ bazel build --spawn_strategy=local --nouse_action_cache --noremote_accept_cached --noremote_upload_local_results --local_ram_resources=HOST_RAM*.5 --local_cpu_resources=HOST_CPUS*.5 //tensorflow/tools/pip_package:build_pip_package
$ bazel shutdown
```

Then, invoke **PersistExt** to parse the Python APIs.

```shell
# -p: The TensorFlow source code folder that needs to be parsed.
# -v: TensorFlow version, must be semantic version (ie a.b.c)
# -t: The file path to store result
$ python main.py -p ./tf_src -v 2.15.0 -t result.json
```

> Option: If users only want to parse and extract the Python APIs, `pip install tensorflow==2.15.0` is just ok. Users only need to replace `./tf_src` with the path to TensorFlow package.

Next, users need to follow the official [CodeQL documentation](https://docs.github.com/en/code-security/codeql-for-vs-code) and [VSCode tutorials](https://marketplace.visualstudio.com/items?itemName=github.vscode-codeql#checking-access-to-the-codeql-cli) to install [CodeQL](https://codeql.github.com/) and configure the relevant [VSCode extensions](https://marketplace.visualstudio.com/items?itemName=github.vscode-codeql#checking-access-to-the-codeql-cli).

Before parsing the C++ side code, we need to compile TensorFlow source code to generate a database for CodeQL query.

```shell
$ cd tf_src/tensorflow-tensorflow-6887368
$ codeql database create new-tensorflow-database --language=cpp --command='path/to/TensorAbuse/PersistExt/codeQL/script/build.sh'
```

Then, we follow [CodeQL query tutorial](https://docs.github.com/en/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries) and select `new-tensorflow-database` as target database. After that, we invoke **extract_x.ql** to parse the C++ side code, marcos and extract all op kernels implementations. After exectuion, the query result can be exported into `csv` or `xlsx` format.

> Tips: If users have no idea how to run `.ql` file, please refer to [vscode-codeql-starter](https://github.com/github/vscode-codeql-starter). Users can directly use the configuration in the `codeql-custom-queries-cpp` folder and replace the `example.ql` file with the `.ql` files in `TensorAbuse/PersisExt/codeQL/query` to successfully run the query of the .ql files.

In the next step, we analyze the previously extracted Python interface code, C++ macro, and C++ OpKernel code to build a complete **Python - C++** cross-language call chain.

```shell
# PersistExt analyze python-C++ cross language call chain
# -b / --base_path: The path to Tensorflow source code folder
$ python main.py -b /path/to/TensorFlow_source_code
```

Before running `main.py`, users need to replace `/path/to/TensorFlow_source_code` with their own path to TensorFlow source code folder.

`main.py` will extract the python interface code from the `PersistExt/excel` folder, as well as the location of the C++ code obtained by codeQL analysis in the TensorFlow source code folder. After that, `main.py` will extract the C++ code, C++ macros, etc., and build a complete set of **python - C++** cross-language call chains together with the previously obtained python interface code, and save them in a newly generated `PersistExt_result.json` file.

## Result

We have pre-analyzed APIs for some TensorFlow versions in the [`PersistExt/results` directory](PersistExt/results). Each line represents the function name, OP name, and the relative file path where the API is located. Additionally, [`PersistExt/API_tf_version_analysis.ipynb` file](PersistExt/API_tf_version_analysis.ipynb) contains information on the presence of ops across different TensorFlow versions.

Besides, `PersistExt_result.json` contains the whole analysis result of PersistExt. For each persistent python API in TensorFlow 2.15.0, we have extracted and analyzed its complete **python - C++** cross-language call chain and display it in this JSON file.

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
# bibtex entry
```
@inproceedings{zhu2025model,
  title={{My Model is Malware to You: Transforming AI Models into Malware by Abusing TensorFlow APIs}},
  author={Zhu, Ruofan and Chen, Ganhao and Shen, Wenbo and Xie, Xiaofei and Chang, Rui},
  booktitle={Proceedings of the 2025 IEEE Symposium on Security and Privacy (S\&P)},
  year={2025},
  organization={IEEE},
  publisher={IEEE},
}
```
