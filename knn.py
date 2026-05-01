#KNearestNeighbors
#Using Euclidean distance

x = [[1,2],[2,3],[2,4],[3,3],[3,4],[4,5],[5,5],[6,6],[6,7],[7,8],[8,8],[8,9]]

y = [0,0,0,0,0,0,1,1,1,1,1,1]

def compute_distances(features, sample):
    distances = []
    for point in features:
        sum_squared_distance = 0
        for i in range(len(point)):
            sum_squared_distance += (sample[i] - point[i]) ** 2
        distances.append(sum_squared_distance ** 0.5)
    return distances

def get_k_nearest(distances, labels, k):
    count = 0
    sorted_indices = sorted(range(len(distances)), key=lambda i: distances[i])
    k_labels = [labels[i] for i in sorted_indices[:k]]
    for lab in k_labels:
        if k_labels.count(lab) > count:
            count = k_labels.count(lab)
            most_common = lab
    return most_common

def predict(sample, features, labels, k=3):
    distances = compute_distances(features, sample)
    return get_k_nearest(distances, labels, k)

print("The most likely value of y for this sample is:", predict([5,6], x, y))
