#Gradient Descent

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 18, 25, 32, 39, 46, 53, 60, 67, 74]

a_try = 3
b_try = 9

def loss(a, b, x, y):
    mean_squared_error = 0
    for idx in range(len(x)):
        mean_squared_error += ((y[idx] - (a * x[idx] + b)) ** 2) / len(x)
    return mean_squared_error

def train_model(a_current, b_current, features, labels):
    for _ in range(10000):
        #training "a"
        a_current_loss = loss(a_current, b_current, features, labels)
        a_next_loss = loss(a_current + 0.01, b_current, features, labels)
        a_improvement = a_current_loss - a_next_loss
        if a_improvement > 0:
            a_current += 0.01
        elif a_improvement < 0:
            a_current -= 0.01
        #training "b"
        b_current_loss = loss(a_current, b_current, features, labels)
        b_next_loss = loss(a_current, b_current + 0.01, features, labels)
        b_improvement = b_current_loss - b_next_loss
        if b_improvement > 0:
            b_current += 0.01
        elif b_improvement < 0:
            b_current -= 0.01       
    return a_current, b_current

def predict(sample, a_b):
    return a_b[0] * sample + a_b[1]

model_params = train_model(a_try, b_try, x, y)

print(predict(11, model_params))