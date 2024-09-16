import h5py
from .issue import Issue, Severity, Category
from .model import Model
import json
from .settings import malicious_op_list
from google.protobuf import json_format
from tensorflow.core.protobuf import saved_model_pb2


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
                            self.issues.append(Issue(Severity.HIGH, Category.LAMBDA_LAYER, f"Lambda layer detected in h5 model, \nlayer: {layer}"))
        except Exception as e:
            print(f"Error scanning h5 model: {e}")
            
    def scan(self):
        self.lambda_scan()
        
        
        
class SavedModelScan(BaseScan):
    def __init__(self, model: Model) -> None:
        super().__init__(model)
        self.issues = []

    def get_op_list(self, model_json: json) -> list[str]:
        model_op_list = set()
        for metagrah in model_json["metaGraphs"]:
            model_op_list.update(node["op"] for node in metagrah["graphDef"]["node"])
            try:
                for func in metagrah["graphDef"]["library"]["function"]:
                    try:
                        model_op_list.update(node["op"] for node in func["nodeDef"])
                    except KeyError:
                        continue
            except KeyError:
                pass
            
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
            print(oplist)
                        
                        
        except Exception as e:
            print(f"Error scanning saved model: {e}")
            
            
    def scan(self):
        self.malicious_op_scan()