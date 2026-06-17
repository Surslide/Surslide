#Linear regression

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 18, 25, 32, 39, 46, 53, 60, 67, 74]

def calculate_loss(slope, intercept, features, labels): #mean squared error
    dataset_size = len(features)
    return sum((label - (slope*feature + intercept)) ** 2 / dataset_size for feature, label in zip(features, labels))

def gradient(features, labels, learning_rate, iterations, dataset_size):
    #math to find a good start point
    slope = (labels[1] - labels[0]) / (features[1] - features[0])
    intercept = labels[0] - slope*features[0]
    #learning
    for _ in range(iterations):
        slope_grad = 0
        intercept_grad = 0
        for feature, label in zip(features, labels):
            error = label - (slope*feature + intercept)
            slope_grad += error * feature / dataset_size
            intercept_grad += error / dataset_size
        slope += slope_grad * learning_rate
        intercept += intercept_grad * learning_rate
    return slope, intercept

class LinearRegression:
    def __init__(self):
        self.features = None
        self.labels = None

    def fit(self, features, labels, learning_rate=0.01, iterations=10000):
        if len(features) != len(labels):
            raise ValueError("Features and labels must have the same size")
        self.features = features
        self.labels = labels
        self.slope, self.intercept = gradient(features, labels, learning_rate, iterations, len(features))
    
    def loss(self):
        if self.features is None or self.labels is None:
            raise ValueError("Model hasn't been fitted yet")
        return(calculate_loss(self.slope, self.intercept, self.features, self.labels))

    def predict(self, samples):
        if self.features is None or self.labels is None:
            raise ValueError("Model hasn't been fitted yet")
        if isinstance(samples, (list, tuple)):
            return [self.slope*sample + self.intercept for sample in samples]
        return self.slope*samples + self.intercept
    
if __name__ == "__main__":
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [11, 18, 25, 32, 39, 46, 53, 60, 67, 74]

    LinReg = LinearRegression()
    LinReg.fit(X, y)

    print("loss: ", LinReg.loss())
    print("prediction: ", LinReg.predict([0,5,11]))