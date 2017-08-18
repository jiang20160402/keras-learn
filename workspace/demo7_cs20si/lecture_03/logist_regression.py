import time
import numpy as numpy
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# Step1: Read in data
# using TF Learn's built in function to load MNIST data to the folder data/mnist
mnist = input_data.read_data_sets("/data/mnist", one_hot=True)

# Step2: Define parameters for the model
learning_rate = 0.1
batch_size = 128
n_epochs = 25

# Step3: create placeholders for features and labels
# each image in the MNIST data is of shape 28*28 = 784
# therefore, each image is rerpresented with a 1*784 tensor
# there are 10 classes for each image, corresponding to digits 0-9.
# each label is one hot vector.
X = tf.placeholder(tf.float32, [batch_size, 784], "name")
Y = tf.placeholder(tf.float32, [batch_size, 10], "label")

# Step4: create weights and bias
# w is initialized to random variables with mean of 0, stddev of 0.01
# b is initialized to 0
# shape of w denpends on the dimension of X and Y so that Y = tf.matmul(X, w)
# shape of b depends on Y
w = tf.Variable(tf.random_normal(shape=[784, 10], stddev=1.0), name="weights")
b = tf.Variable(tf.zeros([1, 10]), name="bias")

# Step5: predict Y from X and w, b
# the model that returns probability distribution of possible label of the image
# through the softmax layer
# a batch_size x 10 tensor that represents the possibility of the digits
logits = tf.matmul(X, w) + b

# Step6: define loss function
# use softmax cross entropy with logits as the loss function
# compute mean cross entropy, softmax is applied internally
entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y, name="loss")
loss = tf.reduce_mean(entropy) # computes the mean over examples in the batch

# Step7: define training op
# using gradient descent with learning rate of 0.01 to minimize cost
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
  writer = tf.summary.FileWriter('./my_graph/logistic_reg', sess.graph)

  start_time = time.time()
  sess.run(init)
  n_batches = int(mnist.train.num_examples/batch_size)
  for i in range(n_epochs):
    total_loss = 0

    for _ in range(n_batches):
      X_batch, Y_batch = mnist.train.next_batch(batch_size)
      _, loss_batch = sess.run([optimizer,loss], feed_dict={X: X_batch, Y: Y_batch})
      total_loss += loss_batch
    print('Average loss epoch {0}: {1}'.format(i, total_loss/n_batches))

  print('Total time: {0} seconds'.format(time.time() - start_time))

  print('Optimization Finished!') # should be around 0.35 after 25 epochs

  # test the model
  # preds = tf.nn.softmax(logits)
  # correct_preds = tf.equal(tf.argmax(preds, 1), tf.argmax(Y, 1))
  correct_preds = tf.equal(tf.argmax(Y, 1), tf.argmax(logits, 1))
  accuracy = tf.reduce_sum(tf.cast(correct_preds, tf.float32))

  n_batches = int(mnist.test.num_examples/batch_size)
  total_correct_preds = 0

  for i in range(n_batches):
    X_batch, Y_batch = mnist.test.next_batch(batch_size)
    accuracy_batch = sess.run(accuracy, feed_dict={X: X_batch, Y: Y_batch})
    total_correct_preds += accuracy_batch

  print('Accuracy {0}'.format(total_correct_preds/mnist.test.num_examples))

  writer.close()
