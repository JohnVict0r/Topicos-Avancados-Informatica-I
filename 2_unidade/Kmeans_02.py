from sklearn.cluster import KMeans

your_model = KMeans(n_clusters=4, init='random')

#Fit
your_model.fit(x_training_data)

#Predict
predictions = your_model.predict(your_x_data)

#Validating the Model
#Import and print accuracy, recall, precision, and F1 score
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

print(accuracy_score(true_labels, guesses))
print(recall_score(true_labels, guesses))
print(precision_score(true_labels, guesses))
print(f1_score(true_labels, guesses))

#Import and print the confusion matrix
from sklearn.metrics import confusion_matrix

print(confusion_matrix(true_labels, guesses))

#Training Sets and Test Sets
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
