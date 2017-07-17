#%%#
import numpy as np
import network

def load_data(path='./workspace/demo2/data/mnist.npz'):
  f = np.load(path)
  x_train, y_train = f['x_train'], f['y_train']
  x_test, y_test = f['x_test'], f['y_test']
  f.close()
  return (x_train, y_train), (x_test, y_test)

def load_data_wrapper():
  (x_train, y_train), (x_test, y_test) = load_data()
  training_inputs = [np.reshape(x, (784, 1)) for x in x_train]
  training_results = [vectorized_result(y) for y in y_train]
  training_data = list(zip(training_inputs, training_results))
  test_inputs = [np.reshape(x, (784, 1)) for x in x_test]
  test_results = [vectorized_result(y) for y in y_test]
  test_data = list(zip(test_inputs, test_results))
  return (training_data, test_data)

def vectorized_result(j):
    """Return a 10-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a digit
    (0...9) into a corresponding desired output from the neural
    network."""
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

training_data, test_data = load_data_wrapper()
net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)