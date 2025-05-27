import tensorflow as tf


dispatcher = tf.data.experimental.service.DispatchServer(config=tf.data.experimental.service.DispatcherConfig(port=1236))
print("config = ", dispatcher._config)
dispatcher_address = dispatcher.target.split("://")[1]
worker = tf.data.experimental.service.WorkerServer(
    tf.data.experimental.service.WorkerConfig(
        dispatcher_address=dispatcher_address))
print("dispatcher.target = ", dispatcher.target, type(dispatcher.target))
print("wait for link to <attacker 's IP address>:1236 ...")

while True:
    a = 1