# Use iris dataset to train KNN model

import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from knn import KNN

cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

iris_dataset = datasets.load_iris()
X, y = iris_dataset.data, iris_dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

plt.figure()
plt.scatter(X[:,2], X[:,3], c=y, cmap=cmap, edgecolor='k', s=20)
plt.show

# Do our classification thing!
clf = KNN(5)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

print(predictions)

# Evaluation accuracy
acc = np.sum(predictions == y_test) / len(y_test)     # <-- the equality test inside sum() is new to me... look it up
print(acc)
