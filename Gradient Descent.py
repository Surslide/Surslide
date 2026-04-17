#Gradient Descent

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 18, 25, 32, 39, 46, 53, 60, 67, 74]

def loss(features, labels, a_b):
    mean_squared_error = 0
    for idx in range(len(features)):
        mean_squared_error += ((labels[idx] - (a_b[0] * features[idx] + a_b[1])) ** 2)
    return mean_squared_error / len(features)

def calculate_vote_a(a, b, features, labels):
    vote_a = 0
    for idx in range(len(features)):
        vote_a += (labels[idx] - (a * features[idx] + b)) * features[idx]
    return vote_a / len(features)

def calculate_vote_b(a, b, features, labels):
    vote_b = 0
    for idx in range(len(features)):
        vote_b += labels[idx] - (a * features[idx] + b)
    return vote_b / len(features)

def train_model(features, labels, learning_rate = 0.01, iterations=10000):
    a_current = 1
    b_current = 1
    for _ in range(iterations):
        #training "a"
        a_current += calculate_vote_a(a_current, b_current, features, labels) * learning_rate
        #training "b"
        b_current += calculate_vote_b(a_current, b_current, features, labels) * learning_rate
    return a_current, b_current

def predict(sample, a_b):
    return a_b[0] * sample + a_b[1]

model_params = train_model(x, y)

print(f"predict: {predict(11, model_params)}\nloss: {loss(x, y, model_params):.20f}")
