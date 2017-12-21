# %% the original question
import tensorflow as tf
n_epochs = 2
batch_size = 3

data = tf.contrib.data.Dataset.range(12)

data = data.repeat(n_epochs)
data = data.batch(batch_size)
next_batch = data.make_one_shot_iterator().get_next()

sess = tf.Session()
for _ in range(4):
    print(sess.run(next_batch))

print("new epoch")
data = data.shuffle(12)
for _ in range(4):
    print(sess.run(next_batch))

# %% my answer
# shuffle all elements
import tensorflow as tf

n_epochs = 2
batch_size = 3
buffer_size = 5

dataset = tf.data.Dataset.range(12)
dataset = dataset.shuffle(buffer_size=buffer_size)
dataset = dataset.batch(batch_size)
dataset = dataset.repeat(n_epochs)
iterator = dataset.make_one_shot_iterator()
next_batch = iterator.get_next()

sess = tf.Session()
print("epoch 1")
for _ in range(4):
    print(sess.run(next_batch))
print("epoch 2")
for _ in range(4):
    print(sess.run(next_batch))

# %%
# shuffle between batches, not shuffle in a batch
import tensorflow as tf

n_epochs = 2
batch_size = 3
buffer_size = 5

dataset = tf.data.Dataset.range(12)
dataset = dataset.batch(batch_size)
dataset = dataset.repeat(n_epochs)
dataset = dataset.shuffle(buffer_size=buffer_size)
iterator = dataset.make_one_shot_iterator()
next_batch = iterator.get_next()

sess = tf.Session()
print("epoch 1")
for _ in range(4):
    print(sess.run(next_batch))
print("epoch 2")
for _ in range(4):
    print(sess.run(next_batch))
