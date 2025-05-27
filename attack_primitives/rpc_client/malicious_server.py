# import socket
# #创建一个TCP/IP socket对象
# server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 绑定socket到本地IP和端口

# server_address=('0.0.0.0',1236)
# server_socket.bind(server_address)

# #监听socket
# server_socket.listen(5)
# while True:
#     print('等待客户端连接...')
#     client_socket, client_address =server_socket.accept()
#     print('接收到客户端连接:', client_address)
#     while True:
#         data = client_socket.recv(1024)
#         if not data:
#             break
#         print('接收到客户端数据:', data)

import tensorflow as tf
from tensorflow.python.ops.gen_experimental_dataset_ops import register_dataset, register_dataset_v2
from tensorflow.python.data.ops.dataset_ops import DatasetV2, DatasetSource
from tensorflow.python.data.experimental.ops.readers import CsvDatasetV2, CsvDatasetV1
import time
import sys
from tensorflow.python.framework import tensor_spec
class tmpclass(DatasetSource):
    def __init__(self, variant_tensor):
        super(tmpclass, self).__init__(variant_tensor)
    @property
    def element_spec(self):
        return tensor_spec.TensorSpec([], tf.string)
@tf.function(input_signature=[
     tf.TensorSpec([], tf.int32),
     tf.TensorSpec([], tf.int32)])
def remote_fn(a, b):
    return tf.add(a, b)
address = "0.0.0.0:{}".format(1235)
server = tf.distribute.experimental.rpc.Server.create("grpc", address)
server.register("MALICIOUS_PAYLOAD", remote_fn)
server.start()
while True:
    pass
