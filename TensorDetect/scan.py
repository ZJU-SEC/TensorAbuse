import h5py
from .issue import Issue, Severity, Category
from .model import Model
import json
from .settings import malicious_op_list, malicious_op_args, malicious_files, safe_ips, args_info
from google.protobuf import json_format
from tensorflow.core.protobuf import saved_model_pb2
from tensorflow.python.keras.protobuf import saved_metadata_pb2 as metadata_pb2
import os
import base64
import fnmatch
import re

class BaseScan:
    def __init__(self, model: Model):
        """
        Initialize a BaseScan object with a Model instance.

        :param model: model instance
        """
        self.model = model

    def scan(self):
        """
        The base scan method to be overridden by derived scan classes.
        """
        raise NotImplementedError("Scan method must be implemented by subclasses")


class H5Scan(BaseScan):
    def __init__(self, model: Model) -> None:
        super().__init__(model)
        self.issues = []
    
    def lambda_scan(self):
        """
        Scan the h5 model for Lambda layers and any malicious operations.
        """
        try:
            with h5py.File(self.model.model_file, 'r') as f:
                if 'model_config' in f.attrs:
                    config = f.attrs['model_config']
                    config = json.loads(config)
                    
                    # lambda_layers = []
                    
                    # Check for Lambda layers in the model configuration
                    for layer in config['config']['layers']:
                        layer_class_name = layer['class_name']
                        if layer_class_name == 'Lambda':
                            # lambda_layers.append(layer)
                            self.issues.append(Issue(Severity.HIGH, Category.LAMBDA_LAYER, f"Lambda layer detected in h5 model, \nlayer: {layer}\n"))
        except Exception as e:
            print(f"Error scanning h5 model: {e}")
            
    def scan(self):
        self.lambda_scan()
        
        
        
class SavedModelScan(BaseScan):
    def __init__(self, model: Model) -> None:
        super().__init__(model)
        self.issues = []
        self.settings = malicious_op_list
        self.settings_args = malicious_op_args
        self.args_info = args_info
    
    # def is_ip(self, s):
    #     ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$')
    #     ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')
    #     if bool(ipv4_pattern.match(s)) or bool(ipv6_pattern.match(s)):
    #         return 1
    #     elif any(bool(ipv4_pattern.match(part)) for part in s.split()) or any(bool(ipv6_pattern.match(part)) for part in s.split()):
    #         return 1
    #     else:
    #         return 0
    
    # def is_filepath(self, s):
    #     path_pattern = re.compile(r'^(?:[a-zA-Z]:[\\/]|[\\/]|\.\/|\.{2}\/)(?:[^<>:"/\\|?*\x00-\x1F]*[\\/])*[^<>:"/\\|?*\x00-\x1F]*$')
    #     if bool(path_pattern.match(s)):
    #         return 1
    #     elif any(bool(path_pattern.match(part)) for part in s.split()):
    #         return 1
    #     else:
    #         return 0
        
    def is_malicious_file(self, filepath):
        if filepath in malicious_files:
            return True
        for pattern in malicious_files:
            if fnmatch.fnmatch(filepath, pattern):
                return True
        return False
    
    def is_safe_ip(self, ip):
        for pattern in safe_ips:
            if fnmatch.fnmatch(ip, pattern):
                return True
        return False
    
    def get_op_list(self, model_json: json) -> list[str]:
        model_op_list = []
        model_op_map = {}
        for metagrah in model_json["metaGraphs"]:
            for node in metagrah["graphDef"]["node"]:
                model_op_list.append(
                    {
                        "name": node["name"],
                        "op": node["op"],
                        "info": node
                    }
                )
                model_op_map[node["name"]] = node
            try:
                for func in metagrah["graphDef"]["library"]["function"]:
                    try:
                        for node in func["nodeDef"]:
                            model_op_list.append(
                                {
                                    "name": node["name"],
                                    "op": node["op"],
                                    "info": node
                                }
                            )
                            model_op_map[node["name"]] = node
                        # model_op_list.update(node for node in func["nodeDef"])
                    except KeyError:
                        continue
            except KeyError:
                pass
        return model_op_list
            
    def malicious_op_scan(self):
        """
        Scan the saved model for Lambda layers and any malicious operations.
        """
        try:
            saved_model = saved_model_pb2.SavedModel()
            with open(self.model.model_file, "rb") as f:
                saved_model.ParseFromString(f.read()) 
                
            json_saved_model = json.loads(json_format.MessageToJson(saved_model))
            oplist = self.get_op_list(json_saved_model)
            for op in oplist:
                if op["op"] in self.settings:
                    issued = 0
                    if "input" in op["info"]:
                        opinfo_input = op["info"]["input"] # all args infomation of an op
                        for arg in opinfo_input:
                            op_arg = arg.split(":")[0] # 'Save/filename:output:0' -> 'Save/filename'
                            if "/" not in op_arg:
                                arg_name = op_arg.split("/")[0]
                            else:
                                arg_name = op_arg.split("/")[1]  # 'Save/filename' -> 'filename'
                            # elif op_arg=="Const":
                            #     for i in range(0, len(oplist)):
                            #         if op_arg==oplist[i]["name"]:
                            #             break
                            #     if oplist[i]["op"]=="Const" and oplist[i]["info"]["attr"]["value"]["tensor"]['dtype']=="DT_STRING":
                            #         base64_arg_value=oplist[i]["info"]["attr"]["value"]["tensor"]["stringVal"]
                            #         arg_value=base64.b64decode(base64_arg_value[0]).decode('utf-8')
                            #         if self.is_malicious_file(arg_value):
                            #             self.issues.append(Issue(Severity.HIGH, Category.TENSOR_ABUSE, f"Tensorabuse op detected with malicious behavior in saved model, \nop: {op};\n{malicious_op_args[op["op"]]}: {arg_value}\n"))                       
                            #         else:
                            #             self.issues.append(Issue(Severity.MID, Category.TENSOR_ABUSE, f"Tensorabuse op detected in saved model, \nop: {op};\n{malicious_op_args[op["op"]]}: {arg_value}\n"))                       
                            #     continue
                            
                            
                            if arg_name in malicious_op_args[op["op"]]:
                                find = 0
                                for i in range(0, len(oplist)):
                                    if op_arg==oplist[i]["name"]:
                                        find = 1
                                        break
                                if find==1:
                                    if oplist[i]["op"]=="Const" and oplist[i]["info"]["attr"]["value"]["tensor"]['dtype']=="DT_STRING":
                                        base64_arg_value=oplist[i]["info"]["attr"]["value"]["tensor"]["stringVal"]
                                        arg_value=base64.b64decode(base64_arg_value[0]).decode('utf-8')
                                        if arg_name in self.args_info["file_args"]and self.is_malicious_file(arg_value):
                                            issued=1
                                            self.issues.append(Issue(Severity.HIGH, Category.TENSOR_ABUSE, f"Tensorabuse op detected with malicious behavior in saved model, \nop: {op};\n{malicious_op_args[op["op"]]}: {arg_value}\n"))                       
                                        elif arg_name in self.args_info["ip_args"] and (not self.is_safe_ip(arg_value)):
                                            issued=1
                                            self.issues.append(Issue(Severity.HIGH, Category.TENSOR_ABUSE, f"Tensorabuse op detected with malicious behavior in saved model, \nop: {op};\n{malicious_op_args[op["op"]]}: {arg_value}\n"))                       
                                        else:
                                            issued=1
                                            self.issues.append(Issue(Severity.MID, Category.TENSOR_ABUSE, f"Tensorabuse op detected in saved model, \nop: {op};\n{malicious_op_args[op["op"]]}: {arg_value}\n"))                       
                                
                    if "attr" in op["info"]:
                        opinfo_attr = op["info"]["attr"]
                        for attr in opinfo_attr:
                            if attr in malicious_op_args[op["op"]]:
                                if "list" in opinfo_attr[attr]:
                                    base64_arg_value=opinfo_attr[attr]["list"]["s"]
                                    arg_value=base64.b64decode(base64_arg_value[0]).decode('utf-8')
                                elif "s" in opinfo_attr[attr]:
                                    base64_arg_value=opinfo_attr[attr]["s"]
                                    arg_value=base64.b64decode(base64_arg_value).decode('utf-8')
                                if not self.is_safe_ip(arg_value):
                                    issued=1
                                    self.issues.append(Issue(Severity.HIGH, Category.TENSOR_ABUSE, f"Tensorabuse op detected with malicious behavior in saved model, \nop: {op};\n{malicious_op_args[op["op"]]}: {arg_value}\n"))                       
                                else:
                                    issued=1
                                    self.issues.append(Issue(Severity.MID, Category.TENSOR_ABUSE, f"Tensorabuse op detected in saved model, \nop: {op};\n{malicious_op_args[op["op"]]}: {arg_value}\n"))                       

                    if not issued:
                        self.issues.append(Issue(Severity.MID, Category.TENSOR_ABUSE, f"Tensorabuse op detected in saved model, \nop: {op};\n"))                       

        except Exception as e:
            print(f"Error scanning saved model: {e}")
        
        
    def lambda_scan(self):
        """
        Scan the saved model for Lambda layers and any malicious operations.
        """
        try:
            if not os.path.exists(self.model.keras_metadata_file):
                return
            saved_metadata = metadata_pb2.SavedMetadata()
            with open(self.model.keras_metadata_file, "rb") as f:
                saved_metadata.ParseFromString(f.read())
            lambda_code = []
            for node in saved_metadata.nodes:
                if node.identifier == "_tf_keras_layer":
                    layer = json.loads(node.metadata)
                    if layer["class_name"] == "Lambda":
                        self.issues.append(Issue(Severity.HIGH, Category.LAMBDA_LAYER, f"Lambda layer detected in h5 model, \nlayer: {layer}\n"))                       
        except Exception as e:
            print(f"Error scanning saved model: {e}")
            
            
    def scan(self):
        self.malicious_op_scan()
        self.lambda_scan()
        
    def print_issues(self):
        for issue in self.issues:
            print(issue)