import tensorflow as tf
import numpy as np

W_loaded = np.load("weights_array.npy")
W_loaded_squeezed = W_loaded.squeeze(axis=0)
tf.Variable(W_loaded_squeezed, name="W")
with tf.Session() as sess:
                sess.run(tf.global_variables_initializer())
                w_array = sess.run([W])
