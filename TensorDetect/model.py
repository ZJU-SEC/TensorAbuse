from enum import Enum
import os
class ModelType(Enum):
    TF_H5 = "Tensorflow h5 model"
    TF_SM = "Tensorflow saved model"
    
class Model:
    def __init__(self, file_path, model_type: ModelType):
        """
        Initialize a Model object with file path and model type (h5 or saved_model).

        :param file_path: file path of models
        :param model_type: model types ('h5' or 'saved_model')
        """
        self.file_path = file_path
        self.model_type = model_type
        self.model_file = self.get_model_file_from_path()

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
            
    



