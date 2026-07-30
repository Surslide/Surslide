#KNearestNeighbors with external libraries
#Euclidean or Manhattan distance

import numpy as np

def compute_distances(sample, features, distance_type):
    distance_type = distance_type.lower()
    distance_type = distance_type.strip()
    if distance_type == "euclidean":
        return np.sqrt(((sample - features) ** 2).sum(axis=1))
    elif distance_type == "manhattan":
        return np.abs(sample - features).sum(axis=1)
    else:
        raise ValueError("Invalid distance type, this model only supports 'euclidean' or 'manhattan'")

def predict_label(distances, labels, k):
    epsilon = 0.00001
    votes = {}
    sorted_idx = np.argsort(distances)
    k_idx = sorted_idx[:k]
    for idx in k_idx:
        if labels[idx] in votes:
            votes[labels[idx]] += 1 / (distances[idx] + epsilon)
        else:
            votes[labels[idx]] = 1 / (distances[idx] + epsilon)
    return max(votes, key=lambda i: votes[i])

class KNN:
    def __init__(self, k=3):
        if not (isinstance(k, int) and k > 0):
            raise ValueError("K must be an 'int' and must be greater than '0'")
        self.k = k
        self.features = None
        self.labels = None

    def fit(self, features, labels):
        self.features = np.array(features)
        self.labels = np.array(labels)
        if len(self.features) != len(self.labels):
            raise ValueError("Features and labels must have the same size")
        if self.k > len(self.labels):
            raise ValueError("K cannot be higher than number of samples")
    
    def predict(self, samples, distance_type="euclidean"):
        samples = np.array(samples)
        if samples.ndim == 1:
            samples = samples.reshape(1, -1)
        elif samples.ndim > 2: 
            raise ValueError("Samples must have shape (samples, features)")
        if self.features is None or self.labels is None:
            raise ValueError("Model hasn't been fitted yet")
        
        results = [predict_label(compute_distances(sample, self.features, distance_type), self.labels, self.k) for sample in samples]
        return np.array(results)

if __name__ == "__main__":
    #features
    X = [[1,2],[2,3],[2,4],[3,3],[3,4],[4,5],[5,5],[6,6],[6,7],[7,8],[8,8],[8,9]]

    #labels
    y = [0,0,0,0,0,0,1,1,1,1,1,1]

    KNN_3 = KNN(3)
    KNN_3.fit(X, y)
    print(KNN_3.predict([5,5], "euclidean"))
    print()
    print(KNN_3.predict([[3,5],[1,2],[8,6]], "manhattan"))
