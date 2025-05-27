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
        a = tf.raw_ops.FixedLengthRecordDatasetV2(filenames = ["./test"], 
                                                record_bytes = 1,
                                                header_bytes = 0,
                                                footer_bytes = 0,
                                                buffer_size = 1024,
                                                metadata = '',
                                                compression_type = '')

        dataset = tmpclass(a)
        iterable = iter(dataset)
        res = ""
        for m in iterable:
            res += m
        tf.print(res)
        return self.a * x + self.b

model = SimpleLinearModel()

result = model.__call__(tf.constant(5.0))

save_dir = 'FixedLengthRecordDatasetV2_local_file'
tf.saved_model.save(model, save_dir)
