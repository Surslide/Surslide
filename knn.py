#KNearestNeighbors
#Using euclidian distance

x = [[2,4],[7,8],[8,9],[1,3],[4,3],[6,5],[2,2],[9,5],[7,6],[1,4]]
y = [0,1,1,0,0,1,0,1,1,0]

#distance calculation
def calculation(sample, point, index):
    calc = []
    for o in range(len(sample)):
        calc.append((sample[o] - point[o]) **2)
    return sum(calc) ** 0.5, y[index]

def distance(sample, features):
    dist = []
    for i, point in enumerate(features):
        dist.append(calculation(sample, point, i))
    return dist

#prediction
def predict(sample, k):
    distance_classification = distance(sample, x)
    distance_classification.sort()
    kclassification = []
    count = 0
    for j in range(k):
        kclassification.append(distance_classification[j][1])
    for val in kclassification:
        if count < kclassification.count(val):
            count = kclassification.count(val)
            result = val
    return result

sample_y= predict([5,4], 3)

print("The most likely value of y for this sample is:", sample_y)