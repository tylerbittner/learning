# Video: https://www.youtube.com/watch?v=rTEtEy5o3X0
"""
Basic idea: For a given point, compute distances to its K nearest neighbors then return
the avg of those points (regression) or the majority class of those points (classification).
We'll build a classifier here.
"""
import numpy as np
from collections import Counter

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum(p2 - p1)** 2)

class KNN:
    def __init__(self, k=3):
        self.k = k
        print(f'Using k={k}')

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):
        # Get distances from all points
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        # Get nearest k
        nearest_indices = np.argsort(distances)[:self.k]
        nearest_labels = [self.y_train[i] for i in nearest_indices]
        print(f'nearest_labels = {nearest_labels}')

        # Return majority label
        most_common = Counter(nearest_labels).most_common()
        print(f'most_common={most_common}')

        # Return label per the iris data set structure
        return most_common[0][0]
