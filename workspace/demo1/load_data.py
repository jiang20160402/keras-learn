#%%#
import numpy as np

def load_data(path='./workspace/demo1/data/mnist.npz'):
  f = np.load(path)
  x_train, y_train = f['x_train'], f['y_train']
  x_test, y_test = f['x_test'], f['y_test']
  f.close()
  return (x_train, y_train), (x_test, y_test)

(x_train, y_train), (x_test, y_test) = load_data()

print(x_train)
print(y_train)