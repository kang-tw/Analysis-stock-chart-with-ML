from tensorflow.python.client import device_lib
import tensorflow as tf

print(device_lib.list_local_devices())