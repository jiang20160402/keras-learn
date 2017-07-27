import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

def huber_loss(labels, predictions, delta=1.0):
  residual = tf.abs(predictions - labels)
  condition = tf.less(residual, delta)
  small_res = 0.5 * tf.square(residual)
  large_res = delta * residual - 0.5 * tf.square(delta)
  return tf.where(condition, small_res, large_res)

DATA_FILE = "slr05.xls"

# Step1: read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1

# Step2: create placeholders for input X (number of fire) and label Y (number of theft)
X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")

# Step3: create weight and bias, initialized to 0
w = tf.Variable(0.0, name="weights_1")
# u = tf.Variable(0.0, name="weights_2")
b = tf.Variable(0.0, name="bias")

# Step4: construct model to predict Y (number of theft) from the number of fire
# Y_predicted = X * X * w + X * u + b
Y_predicted = X * w + b


# Step5: use the square error as the loss function
# loss = tf.square(Y - Y_predicted, name="loss")
loss = huber_loss(Y, Y_predicted, 1.0)

# Step6: using gradient descent with learning rate of 0.001 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

with tf.Session() as sess:
  # Step7: initialize the necessary variables, in this case, w an b
  sess.run(tf.global_variables_initializer())
  # writer = tf.summary.FileWriter('./my_graph/03/linear_reg', sess.graph)

  # Step8: train the model
  for i in range(100): #run 100 epochs
    total_loss = 0
    for x, y in data:
      # Session runs train_op to minimize loss
      _, l = sess.run([optimizer, loss], feed_dict={X: x, Y: y})
      total_loss += l
    print('Epoch {0}: {1}'.format(i, total_loss/n_samples))

  # close the writer when you're done using it
  # writer.close()

  # Step9: output the values of w and b
  w_value, b_value = sess.run([w, b])

# plot the results
X, Y = data.T[0], data.T[1]
plt.plot(X, Y, 'bo', label='Real data')
plt.plot(X, X * w_value + b_value, 'r', label='Predicted data')
plt.legend()
plt.show()