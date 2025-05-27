import tensorflow as tf
from tensorflow.python.data.ops.dataset_ops import DatasetV2, DatasetSource
from tensorflow.python.data.experimental.ops.readers import CsvDatasetV2, CsvDatasetV1

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
        
        # dataset = tf.data.experimental.CsvDataset(
        #   "/etc/passwd",
        #   [tf.string,  # Required field, use dtype or empty tensor
        #   tf.string,  # Optional field, default to 0.0
        #   tf.string,  # Required field, use dtype or empty tensor
        #   tf.string,
        #   tf.string,
        #   tf.string,
        #   tf.string,
        #   ],
        #   select_cols=[0,1,2,3,4,5,6],
        #   field_delim= ":",
        #   na_value= "?",
        # )
        
        # iterable = iter(dataset)
        # # while(iterable):
        # tf.print(next(iterable))
        # tf.print(next(iterable))
        # # tf.print(next(iterable))

        dataset = tf.data.experimental.CsvDataset("./tmp.csv", [tf.string,tf.string,tf.string], select_cols=[0,1,2], field_delim=":")
        iterable = iter(dataset)
        # while(iterable):
        tf.print(next(iterable))
        tf.print(next(iterable))
        # tf.print(next(iterable))
        # filenames = ["./tmp.csv"]
        # compression_type = tf.constant('', dtype=tf.string)
        # buffer_size = tf.constant(1024, dtype=tf.int64)
        # header = tf.constant(True, dtype=tf.bool)
        # field_delim = tf.constant(',', dtype=tf.string)
        # use_quote_delim = tf.constant(True, dtype=tf.bool)
        # na_value = tf.constant('', dtype=tf.string)
        # select_cols = tf.constant([1,2,3], dtype=tf.int64)
        # record_defaults = [tf.constant([], dtype=tf.string),  
        #                 tf.constant([], dtype=tf.string),  
        #                 tf.constant([], dtype=tf.string)]  
        # exclude_cols = tf.constant([], dtype=tf.int64)
        # output_shapes = [tf.TensorShape([]), tf.TensorShape([]), tf.TensorShape([])]
        # dataset = tf.raw_ops.CSVDatasetV2(
        #     filenames=filenames,
        #     compression_type=compression_type,
        #     buffer_size=buffer_size,
        #     header=header,
        #     field_delim=field_delim,
        #     use_quote_delim=use_quote_delim,
        #     na_value=na_value,
        #     select_cols=select_cols,
        #     record_defaults=record_defaults,
        #     exclude_cols=exclude_cols,
        #     output_shapes=output_shapes
        # )
        # for row in dataset:
        #     print(row)

        # Only parse last three columns
        return self.a * x + self.b

# 实例化模型
model = SimpleLinearModel()       
result = model(tf.constant(5.0))

save_dir = 'CsvDataset_raw'
tf.saved_model.save(model, save_dir)
