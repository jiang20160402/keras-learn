#%%#
import cv2
import matplotlib.pyplot as plt
import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D

def visualize_cat(cat_batch):
  cat = np.squeeze(cat_batch, axis=0)
  print(cat.shape)
  plt.imshow(cat)

cat = cv2.imread('./workspace/demo6/cat.png')
plt.imshow(cat)
cat.shape

model = Sequential()
model.add(Conv2D(3, kernel_size=(3,3), input_shape=cat.shape))
cat_batch = np.expand_dims(cat, axis=0)
conv_cat = model.predict(cat_batch)

visualize_cat(conv_cat)

#%%#
import cv2
import matplotlib.pyplot as plt
import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Activation

def nice_cat_printer(model, cat):
  '''prints the cat as a 2d array'''
  cat_batch = np.expand_dims(cat, axis=0)
  conv_cat2 = model.predict(cat_batch)

  conv_cat2 = np.squeeze(conv_cat2, axis=0)
  print(conv_cat2.shape)
  conv_cat2 = conv_cat2.reshape(conv_cat2.shape[:2])
  print(conv_cat2.shape)
  plt.imshow(conv_cat2)

cat = cv2.imread('./workspace/demo6/cat.png')
plt.imshow(cat)
cat.shape

model = Sequential()
model.add(Conv2D(1, kernel_size=(3,3), input_shape=cat.shape))
model.add(Activation('relu'))

nice_cat_printer(model, cat)