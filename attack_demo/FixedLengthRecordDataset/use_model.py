import tensorflow as tf

save_dir = 'saved_model'
model = tf.saved_model.load(export_dir=save_dir)
result = model(tf.constant(5.0))
