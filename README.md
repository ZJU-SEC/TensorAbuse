# TensorAbuse
This is a TenserAbuse toolkit, which includes tools for analyzing TensorFlow APIs and detecting malicious models.
* PersistExt (Persistent API extraction): This is a tool for analyzing TensorFlow source code. It extracts persistent APIs, corresponding op names, and function source code, allowing further capability analysis by LLMs (Large Language Models).

* CapAnalysis (Capability analysis): This is a tool that leverages LLMs to analyze API capabilities. It constructs prompts using a chain-of-thought approach and supports few-shot prompting for analysis. The process involves two rounds of querying the LLM.

* TensorDetect (TensorAbuse attack detection): This tool is designed to detect malicious TensorFlow models. Currently, it can identify attacks embedded within Lambda layers and TensorAbuse-type exploits.