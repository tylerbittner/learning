"""
Steps to train a LinearRegression model:
    1. init weights & bias to zero
    Given a data point:
        2. predict result with y^ = wx + b
        3. calculate error (MSE)
        4. use gradient descent to update weight & bias values
            4a. get derivatives
                dw = (1/n) * sum(X * (y^ - y))
                db = (1/n) * sum(y^ - y)
            4b. Update w&b with learning rate
        6. repeat n times
Predicting aka testing:
    Given a data point, put values from data point in line equation y^ = wx + b
"""
import numpy as np

class LinearRegression:

    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        # Values we're going to predict
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # Init w&b to zero
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            # Predict y^
            y_pred = np.dot(X, self.weights) + self.bias

            # Get next w&b values with gradient descent
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))  # Note we need the TRANSPOSE of X in the dot product here
            db = (1/n_samples) * np.sum(y_pred - y)
            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred
