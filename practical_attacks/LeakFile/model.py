import tensorflow as tf
from tensorflow.python.data.ops.dataset_ops import DatasetV2, DatasetSource
from tensorflow.python.framework import tensor_spec


# load malicious Tensorflow model locally
save_dir = 'model/LeakFile/saved_model'
model = tf.saved_model.load(export_dir=save_dir)
result = model(tf.constant(5.0))
