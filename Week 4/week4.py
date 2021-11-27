import numpy as np
from numpy.lib.function_base import disp


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
        # TODO
        data = self.data
        p = self.p
        dist = []
        for i in range(len(x)):
            temp_dist=[]
            for j in range(len(data)):
                d = 0
                for k in range(len(data[j])):
                    d+= abs(x[i][k]-data[j][k])**p
                temp_dist.append(d**(1/p))
            dist.append(temp_dist)
        return dist

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
        # TODO
        k_neigh = self.k_neigh
        dist = self.find_distance(x)
        neigh = []
        ind=[]
        for i in dist:
            neigh.append((sorted(i)[:k_neigh]))
        for i in range(len(dist)):
            temp_ind=[]
            for k in neigh[i]:
                for l in range(len(dist[i])):
                    if k == dist[i][l]:
                        temp_ind.append(l)
                        break
            ind.append(temp_ind)
        return tuple([neigh,ind])

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """
        # TODO
        k_neigh=self.k_neighbours(x)
        targets = self.target
        weight = self.weighted
        lst=[]
        wts={}
        mk=0
        for j in range (len(k_neigh[0])):
            if(weight):
                for i in range (len(k_neigh[0][0])):
                    if(targets[k_neigh[1][j][i]] in wts):
                        wts[targets[k_neigh[1][j][i]]]+=(1/(k_neigh[0][j][i]+0.00000001))
                    else:
                        wts[targets[k_neigh[1][j][i]]]=(1/(k_neigh[0][j][i]+0.00000001))
                m=list(wts.values())[0]
                mk=list(wts.keys())[0]
                for key,val in wts.items():
                    if(val>m):
                        m=val
                        mk=key
            else:
                for i in range (len(k_neigh[0][0])):
                    if(targets[k_neigh[1][j][i]] in wts):
                        wts[targets[k_neigh[1][j][i]]]+=1
                    else:
                        wts[targets[k_neigh[1][j][i]]]=1
                m=list(wts.values())[0]
                mk=list(wts.keys())[0]
                for key,val in wts.items():
                    if(val>m):
                        m=val
                        mk=key 
            lst.append(mk)
        return lst

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
        # TODO
        predict=self.predict(x)
        correct,total=0,0
        for i in range(len(y)):
            total+=1
            if(predict[i]==y[i]):
                correct+=1
        accuracy = (correct/total)*100
        return accuracy
