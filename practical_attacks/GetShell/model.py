import tensorflow as tf


# load malicious Tensorflow model locally

save_dir = 'model/GetShell/saved_model'
model = tf.saved_model.load(export_dir=save_dir)
result = model(tf.constant(5.0))
