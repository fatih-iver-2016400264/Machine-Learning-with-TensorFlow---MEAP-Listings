raw_data = nr.random.normal(10, 1, 100)

with tf.session() as sess:
    for i in range(len(raw_data)):
        curr_avg = sess.run(update_avg, feed_dict = {curr_value:raw_data[i]} )