# Imports
import matplotlib.pyplot as plt
import numpy as np
from keras.datasets import cifar10

# CIFAR-10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Target classes: numbers to text
classes = {
  0: 'airplane',
  1: 'automobile',
  2: 'bird',
  3: 'cat',
  4: 'deer',
  5: 'dog',
  6: 'frog',
  7: 'horse',
  8: 'ship',
  9: 'truck'
}

# Visualize 20 random samples
for i in np.random.randint(0, len(x_train)-1, 20):
    # Get data
    sample = x_train[i]
    target = y_train[i][0]
    # Set figure size and axis
    plt.figure(figsize=(1.75, 1.75))
    plt.axis('off')
    # Show data
    plt.imshow(sample)
    plt.title(f'{classes[target]}')
    #plt.savefig(f'./{i}.jpg')