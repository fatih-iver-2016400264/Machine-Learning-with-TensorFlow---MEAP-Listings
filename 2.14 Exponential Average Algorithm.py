import tensorflow as tf
import numpy as np

# Create a vector of 100 numbers with a mean of 10 and stardard deviation of 1
raw_data = np.random.normal(10, 1, 100)

# Define alpha as constant
alpha = tf.constant(0.05)

# A placeholder is just like a variable, but the value is injected from the sesion
curr_value = tf.placeholder(tf.float32)
# Initialize the previous average to zero
prev_avg = tf.Variable(0.)
update_avg = alpha * curr_value + (1 - alpha) * prev_avg

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    # Loop through the data one-by-one to update the average
    for i in range(len(raw_data)):
        curr_avg = sess.run(update_avg, feed_dict = {curr_value: raw_data[i]})
        sess.run(tf.assign(prev_avg, curr_avg))
        print(raw_data[i], curr_avg)