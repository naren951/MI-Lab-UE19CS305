import numpy as np
from numpy.core.records import find_duplicate
from numpy.lib.shape_base import _tile_dispatcher


class KNN:
    """
    K Nearest Neighbours model
    Args:
        k_neigh: Number of neighbours to take for prediction
        weighted: Boolean flag to indicate if the nieghbours contribution
                  is weighted as an inverse of the distance measure
        p: Parameter of Minkowski distance
    """

    def __init__(self, k_neigh, weighted=False, p=2):

        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix( M data points with D attributes each)(float)
            target: Vector of length M (Target class for all the data points as int)
        Returns:
            The object itself
        """

        self.data = data
        self.target = target.astype(np.int64)

        return self

    def find_distance(self, x):
        """
        Find the Minkowski distance to all the points in the train dataset x
        Args:
            x: N x D Matrix (N inputs with D attributes each)(float)
        Returns:
            Distance between each input to every data point in the train dataset
            (N x M) Matrix (N Number of inputs, M number of samples in the train dataset)(float)
        """
        n, _ = self.data.shape
        m, _ = x.shape
        d = np.zeros((n, m))
        for i in range(n):
            n0 = self.data[i]
            for j in range(m):
                n1 = x[j]
                diff = n0 - n1
                s = np.sum(np.power(np.abs(diff), self.p))
                d[i, j] = np.power(s, 1 / self.p)
        return np.transpose(d)

    def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neigh_dists, idx_of_neigh)
            neigh_dists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            idx_of_neigh -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input

            Note that each row of both neigh_dists and idx_of_neigh must be SORTED in increasing order of distance
        """
        dist = self.find_distance(x)
        dists = []
        idx = []
        for i in range(dist.shape[0]):
            d = dist[i]
            en_d = list(enumerate(d))
            en_d.sort(key = lambda x: x[1])
            topk = en_d[0:self.k_neigh]
            idx.append(list((j[0] for j in topk)))
            dists.append(list((j[1] for j in topk)))
        return (np.array(dists), np.array(idx))

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """
        dists, ids = self.k_neighbours(x)
        pred = []
        if not self.weighted:
            dists = np.ones(dists.shape)
        classes = np.unique(self.target)
        for p in range(x.shape[0]):
            res = {clas: 0 for clas in classes}
            for i, d in zip(ids[p], dists[p]):
                res[self.target[int(i)]] += 1 / (d + 0.0000000000001)
            p = list(res.items())
            p.sort(reverse = True, key = lambda x: x[1])
            pred.append(p[0][0])
        return pred

    def evaluate(self, x, y):
        """
        Evaluate Model on test data using 
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix(float)
            y: True target of test data(int)
        Returns:
            accuracy : (float.)
        """
        pred = self.predict(x)
        res = pred == y
        pos = np.sum(res)
        accuracy = pos / len(res) * 100
        return accuracy
