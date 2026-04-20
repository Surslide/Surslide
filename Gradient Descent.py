#Gradient descent

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 18, 25, 32, 39, 46, 53, 60, 67, 74]

def loss(features, labels, a_b):
    mean_squared_error = 0
    for idx in range(len(features)):
        mean_squared_error += ((labels[idx] - (a_b[0] * features[idx] + a_b[1])) ** 2)
    return mean_squared_error / len(features)

def gradient(a, b, features, labels):
    a_grad = 0
    b_grad = 0
    for idx in range(len(features)):
        error = labels[idx] - (a * features[idx] + b)
        a_grad += error * features[idx]
        b_grad += error
    return a_grad / len(features), b_grad / len(features)

def train_model(features, labels, learning_rate=0.01, iterations=10000):
    a_current = 1
    b_current = 1
    for _ in range(iterations):
        a_grad, b_grad = gradient(a_current, b_current, features, labels)
        a_current, b_current = a_current + a_grad * learning_rate, b_current + b_grad * learning_rate
    return a_current, b_current

def predict(sample, a_b):
    return a_b[0] * sample + a_b[1]

model_params = train_model(x, y)

print(f"predict: {predict(11, model_params)}\nloss: {loss(x, y, model_params):.20f}")
