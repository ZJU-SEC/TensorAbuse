from enum import Enum
import os
import zipfile
import tempfile
class ModelType(Enum):
    TF_H5 = "Tensorflow h5 model"
    TF_SM = "Tensorflow saved model"
    
class Model:
    def __init__(self, path):
        """
        Initialize a Model object with file path and model type (h5 or saved_model).

        :param file_path: file path of models
        """
        self.file_path = path
        
        if path.endswith(".zip"):
            extract_path = tempfile.mkdtemp()  # Create a temporary directory
            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)  # Extract the zip file
            path = extract_path  # Set path to the extracted folder
            
        if path.endswith(".h5"):
            self.model_type = ModelType.TF_H5
        elif os.path.isdir(path) and os.path.exists(os.path.join(path, "saved_model.pb")):
            self.model_type = ModelType.TF_SM
        elif path.endswith("saved_model.pb"):
            self.model_type = ModelType.TF_SM
        else:
            print("Invalid model type!")
            return
        self.model_file = self.get_model_file_from_path()
        self.keras_metadata_file = "{}/keras_metadata.pb".format(os.path.dirname(self.model_file))

    def get_file_info(self):
        """        
        Return a summary of the model file information.
        """
        return {
            "file_path": self.file_path,
            "model_type": self.model_type
        }
    def get_model_file_from_path(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Model file not found at path: {self.file_path}")
        if self.model_type == ModelType.TF_H5:
            return self.file_path
        elif self.model_type == ModelType.TF_SM:
            return os.path.join(self.file_path, "saved_model.pb")
        
        
            
    



