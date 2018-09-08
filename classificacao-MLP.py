import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('datasets/cancer.csv')

X = dataset.iloc[:,[1,2,3,4,5,6,7,8,9]].values
y = dataset.iloc[:, 10].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

import keras
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense( activation = 'relu', input_dim = 8, units = 16, kernel_initializer = 'uniform'))

# Adding the second hidden layer
classifier.add(Dense( activation = 'relu', units = 6, kernel_initializer = 'uniform' ))

# Adding the output layer
classifier.add(Dense( activation = 'sigmoid', units = 1, kernel_initializer = 'uniform'))

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

classifier.fit(X_train, y_train, batch_size = 10, epochs = 40)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

print("Matriz de Confusão:")
print(cm)
print("Taxa de acerto:")
print((cm[0,0]+cm[1,1])/len(y_test) )
print(len(y_test))