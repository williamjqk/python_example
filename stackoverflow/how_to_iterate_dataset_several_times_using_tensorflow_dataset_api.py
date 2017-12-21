# %% questioner's code
import tensorflow as tf
tf.__version__
dataset = tf.contrib.data.Dataset.range(100)
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()
sess = tf.Session()
epoch = 10

for i in range(epoch):
   for j in range(100):
      value = sess.run(next_element)
      assert j == value
      print(j)

# %% my answer
import tensorflow as tf

epoch = 10
dataset = tf.data.Dataset.range(100)
dataset = dataset.shuffle(buffer_size=100) # comment this line if you don't want to shuffle data
dataset = dataset.batch(batch_size=32)     # batch_size=1 if you want to get only one element per step
dataset = dataset.repeat(epoch)
iterator = dataset.make_one_shot_iterator()
next_element = iterator.get_next()

num_batch = 0
with tf.train.MonitoredTrainingSession() as sess:
    while not sess.should_stop():
        value = sess.run(next_element)
        # print(value)
        num_batch += 1
        print("Num Batch: ", num_batch)
