#Linear Regression using grid search
#Testing all possibilities to find the closest a, b

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [15, 22, 29, 36, 43, 50, 57, 64, 71, 78]

#tries
possible_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
possible_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def error_calculation(features, labels, a, b):
    mean_squared_error = 0
    for idx in range(len(labels)):
        mean_squared_error += ((labels[idx] - (a * features[idx] + b)) ** 2) / len(labels)
    return mean_squared_error

def model_creation(features, labels, a_list, b_list):
    best_error = float("inf")
    best_a = 0
    best_b = 0
    for a_attempt in a_list:
        for b_attempt in b_list:
            error = error_calculation(features, labels, a_attempt, b_attempt)
            if error < best_error:
                best_error = error
                best_a = a_attempt
                best_b = b_attempt
    return best_a, best_b

def predict(sample, a_b):
    y_pred = a_b[0] * sample + a_b[1]
    print(y_pred)

lin_grid = model_creation(x, y, possible_a, possible_b)

predict(11, lin_grid)
