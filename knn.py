#KNearestNeighbors
#Using Euclidean distance

x = [[1,2],[2,3],[2,4],[3,3],[3,4],[4,5],[5,5],[6,6],[6,7],[7,8],[8,8],[8,9]]

y = [0,0,0,0,0,0,1,1,1,1,1,1]

def distance(features, labels, sample):
    distance_value = []
    for idx, point in enumerate(features):
        sum_squared_distance = 0
        for idx2, value in enumerate(point):
            sum_squared_distance += (sample[idx2] - value) ** 2
        distance_value.append([sum_squared_distance ** 0.5, labels[idx]])
    return distance_value
       
def predict(sample, k, features, labels):
    k_chosen = []
    count = 0
    distance_classification = distance(features, labels, sample)
    distance_classification.sort()
    for i in range(k):
        k_chosen.append(distance_classification[i][1])
    for o in k_chosen:
        if k_chosen.count(o) > count:
            count = k_chosen.count(o)
            y_pred = o
    return y_pred

sample_y = predict([5,6], 3, x, y)

print("The most likely value of y for this sample is:", sample_y)
