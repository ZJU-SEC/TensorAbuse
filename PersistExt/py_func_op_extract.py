import ast
import os
import astunparse
import json
import argparse

class PyFuncOpExtract:
    def __init__(self, version, path):
        self.version = version # 1 or 2 tensorflow version
        self.path = path # tensorflow source code path
        self.results = []
        
    def analyze_file(self, file_path):
        results = []
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read())
                for node in ast.iter_child_nodes(tree):
                    if isinstance(node, ast.FunctionDef):             
                        # Check for the function calls within the function body
                        for stmt in ast.walk(node):
                            if isinstance(stmt, ast.Call):
                                func = stmt.func
                                if isinstance(func, ast.Attribute):
                                    # Check for _pywrap_tensorflow.TFE_Py_FastPathExecute
                                    if self.version == 1:
                                        if func.attr == "TFE_Py_FastPathExecute" and \
                                            isinstance(func.value, ast.Name) and \
                                                (func.value.id == "_pywrap_tensorflow" or func.value.id == "pywrap_tfe"):
                                            op_name = stmt.args[2].value
                                            results.append({
                                                "name": node.name,
                                                "code": astunparse.unparse(node),
                                                "op_name": op_name
                                            })
                                            break
                                        # Check for _apply_op_helper
                                        elif (func.attr == "apply_op" or func.attr == "_apply_op_helper") and \
                                            isinstance(func.value, ast.Name) and \
                                                func.value.id == "_op_def_lib":
                                            op_name = stmt.args[0].value
                                            results.append({
                                                "name": node.name,
                                                "code": astunparse.unparse(node),
                                                "op_name": op_name
                                            })
                                            break
                                    elif self.version == 2:
                                         # Check for _pywrap_tensorflow.TFE_Py_FastPathExecute
                                        if func.attr == "TFE_Py_FastPathExecute" and \
                                            isinstance(func.value, ast.Name) and \
                                                (func.value.id == "_pywrap_tensorflow" or func.value.id == "pywrap_tfe"):
                                            op_name = stmt.args[2].value
                                            results.append({
                                                "name": node.name,
                                                "code": astunparse.unparse(node),
                                                "op_name": op_name
                                            })
                                            break
                                        # Check for _apply_op_helper
                                        elif func.attr == "_apply_op_helper" and \
                                            isinstance(func.value, ast.Name) and \
                                                (func.value.id == "_op_def_lib" or func.value.id == "_op_def_library"):
                                            op_name = stmt.args[0].value
                                            results.append({
                                                "name": node.name,
                                                "code": astunparse.unparse(node),
                                                "op_name": op_name
                                            })
                                            break
            except Exception as e:
                return []
        return results
    
    def analyze_tensorflow_source(self):
        for subdir, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(subdir, file)
                    result = self.analyze_file(filepath)
                    if result:
                        self.results.extend(result)
    
    def get_results(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)
        return self.results


# # test
# if __name__ == "__main__":
#     path = "./tf2_10_src"
#     version = 2
#     py_func_op_extract = PyFuncOpExtract(version, path)
#     py_func_op_extract.analyze_tensorflow_source()
#     results = py_func_op_extract.get_results()
