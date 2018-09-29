import numpy as np 
import tensorflow as tf 

d = tf.constant(3)
sess = tf.Session()
print(sess.run(d))