#KNearestNeighbors with external libraries
#Using Euclidean distance

from collections import Counter
import numpy as np

X = np.array([[1,2],[2,3],[2,4],[3,3],[3,4],[4,5],[5,5],[6,6],[6,7],[7,8],[8,8],[8,9]])

y = np.array([0,0,0,0,0,0,1,1,1,1,1,1])

def compute_distances(features, sample):
    distances = (features - sample) ** 2
    distances = distances.sum(axis=1)
    return np.sqrt(distances)

def get_k_nearest(distances, labels, k):
    sorted_indices = np.argsort(distances)
    k_labels = labels[sorted_indices[:k]]
    return Counter(k_labels).most_common(1)[0][0]

def predict(sample, features, labels, k=3):
    sample = np.array(sample)
    distances = compute_distances(features, sample)
    return get_k_nearest(distances, labels, k)

print("The most likely value of y for this sample is:", predict([5,6], X, y))
