raw_data = np.random.normal(10, 1, 100)

with tf.Session() as sess:
    for i in range(len(raw_data)):
        curr_avg = sess.run(update_avg , feed_dict = {curr_value:raw_data[i]})
        sess.run(tf.assign(prev_avg, curr_avg))