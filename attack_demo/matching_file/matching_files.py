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
        self.pattern = "./*.py"

    @tf.function
    def __call__(self, x):
        res = tf.raw_ops.MatchingFiles(pattern=self.pattern) # get /home/* to search directory
        # res2 = tf.raw_ops.ExperimentalMatchingFilesDataset(patterns=self.pattern) # get file
        # res3 = tf.raw_ops.MatchingFilesDataset(patterns=self.pattern) # get file
        tf.print(res)
        # dataset2 = tmpclass(res2)
        # iterable2 = iter(dataset2)
        # for a in iterable2:
        #     tf.print(a)
        
        # dataset3 = tmpclass(res3)
        # iterable3 = iter(dataset3)
        # for b in iterable3:
        #     tf.print(b)
# 保存模型
        return self.a * x + self.b

# 实例化模型
model = SimpleLinearModel()       
result = model.__call__(tf.constant(5.0))

save_dir = 'MatchingFiles'
tf.saved_model.save(model, save_dir)