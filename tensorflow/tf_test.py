import tensorflow as tf
t = tf.constant(42.0)
sess = tf.Session()
with sess.as_default():   # or `with sess:` to close on exit
    assert sess is tf.get_default_session()
    assert t.eval() == sess.run(t)
# %%
import numpy as np
np.nan
np.nan == np.nan

# %%
t = tf.constant(42.0)
u = tf.constant(37.0)
tu = tf.multiply(t, u)
ut = tf.multiply(u, t)
with sess.as_default():
   tu.eval()  # runs one step
   ut.eval()  # runs one step
   sess.run([tu, ut])  # evaluates both tensors in a single step
