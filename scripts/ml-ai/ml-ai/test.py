import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd

# load the model
model = keras.models.load_model('model.h5')

# load the test data
dataframe = pd.read_csv('testdata.csv')
data = dataframe.values

# split into input (X) and output (Y) variables
X = data[:,0:8]
Y = data[:,8]

# predict the output for the test data
predictions = model.predict_classes(X)

# calculate the accuracy of the predictions
accuracy = np.mean(predictions == Y)
print('Accuracy: %.2f' % (accuracy*100))