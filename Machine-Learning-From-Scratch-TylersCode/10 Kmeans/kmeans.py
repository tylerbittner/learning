"""
K means algo

Steps:
- Init: assign centroids to random points
- Repeat until max_iters or converged:
    - Assign each point to its closest centroid to create k clusters
    - Update centroids to mean of points in clusters
"""

import numpy as np

class KMeans:
    def __init__(self, K=3, max_iters=100, plot_steps=False):
        self.k = K
        self.max_iters = max_iters
        self.clusters = []

    def predict(self, X):
        self.X = X
        self.n_samples = len(X)
        print(f'self.n_samples={self.n_samples}')
        print(f'X types = {type(X[0])}')

        # init clusters
        self.clusters = [[] for _ in range(self.n_samples)]


        for _ in range(self.n_samples):
            pass




# Test data
data_tuples = [(12,39), (20,36), (28,30), (18,52), (29,54), (33,46), (24,55), (45,59), (45,63),
(52,70), (51,66), (52,63), (55,58), (53,23), (51,14), (61,8), (64,19), (69,71), (72,24)]

# Testing
if __name__ == "__main__":
    np.random.seed(42)
    from sklearn.datasets import make_blobs

    X, y = make_blobs(
        centers=3, n_samples=500, n_features=2, shuffle=True, random_state=40
    )
    print(X.shape)

    clusters = len(np.unique(y))
    print(f'k={clusters}')

    k = KMeans(K=clusters, max_iters=150, plot_steps=False)
    y_pred = k.predict(X)

    # k.plot()