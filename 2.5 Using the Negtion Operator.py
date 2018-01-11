import tensorflow as tf

x = tf.constant([[1, 2]])
neg_x = tf.negative(x)
print(neg_x)