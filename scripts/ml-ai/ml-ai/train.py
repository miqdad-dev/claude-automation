import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd

# load the training data
dataframe = pd.read_csv('data.csv')
data = dataframe.values

# split into input (X) and output (Y) variables
X = data[:,0:8]
Y = data[:,8]

# define the keras model
model = keras.Sequential([
    keras.layers.Dense(12, input_dim=8, activation='relu'),
    keras.layers.Dense(8, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, Y, epochs=150, batch_size=10, verbose=0)

# save the model
model.save('model.h5')