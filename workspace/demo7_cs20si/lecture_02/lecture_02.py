'''
use TensorBoard to visualize graph
'''
# import tensorflow as tf

# a = tf.constant(2, name="a")
# b = tf.constant(3, name="b")
# x = tf.add(a, b, name="add")
# with tf.Session() as sess:
#   writer = tf.summary.FileWriter('./graphs', sess.graph)
#   print(sess.run(x))
#   # close the writer when you’re done using it
#   writer.close()

'''
more constants
'''
# import tensorflow as tf

# a = tf.constant([2, 2], name="a")
# b = tf.constant([[0, 1], [2, 3]], name="b")
# x = tf.add(a, b, name="add")
# y = tf.multiply(a, b, name="multiply")
# with tf.Session() as sess:
#   writer = tf.summary.FileWriter('./graphs', sess.graph)
#   x, y = sess.run([x, y])
#   print(x,y)
#   writer.close()

#%%#
# import tensorflow as tf 
# my_const = tf.constant([1.0, 2.0], name="my_const")
# with tf.Session() as sess:
#   print(sess.graph.as_graph_def())

#%%#
# W = tf.Variable(tf.truncated_normal([700, 10]))
# with tf.Session() as sess:
#   sess.run(W.initializer)
#   print(W)
#   print(W.eval())

#%%#
# W = tf.Variable(10)
# assign_op = W.assign(100)
# with tf.Session() as sess:
#   sess.run(W.initializer)
#   print(W.eval())
#   sess.run(assign_op)
#   print(W.eval())

#%%#
# my_var = tf.Variable(2, name="my_var")
# my_var_times_two = my_var.assign(2 * my_var)
# with tf.Session() as sess:
#   sess.run(my_var.initializer)
#   print(my_var.eval())
#   sess.run(my_var_times_two)
#   print(my_var.eval())  
#   sess.run(my_var_times_two)
#   print(my_var.eval())

#%%#
# '''
# Placeholders
# '''
# a = tf.placeholder(tf.float32, shape=[3])
# b = tf.constant([5,5,5], tf.float32)
# c = a + b 
# with tf.Session() as sess:
#   print(sess.run(c, {a: [1, 2, 3]}))


#%%#
'''
Lazy loading Example
'''
import tensorflow as tf
x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')
z = tf.add(x,y)
with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  writer = tf.summary.FileWriter('./my_graph/12', sess.graph)
  for _ in range(10):
    sess.run(z)
  writer.close()