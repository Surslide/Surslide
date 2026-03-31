#Linear Regression using grid search
#Testing all possibilities to find the closest a, b

#y = grades , x = hours of study
x = [1,2,3,4,5]
y = [19,36,53,70,87]

possible_a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
possible_b = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def calculation(x, a, b):
    y_calc = a * x + b
    return y_calc

def test_error(a, b):
    total_error = 0
    for i in range(len(y)):
        total_error += (y[i] - calculation(x[i], a, b)) ** 2
    return total_error

#for each a, for each b, calculates the error and saves the best combination
def best_parameters(test_a, test_b):
    best_error = float("inf")
    for a in test_a:
        for b in test_b:
            e = test_error(a, b)
            if e < best_error:
                best_error = e
                best_test_a = a
                best_test_b = b
    return best_error, best_test_a, best_test_b

error, a, b = best_parameters(possible_a, possible_b)

print(f"The closest function is: y = {a}x + {b}\nTotal squared error of: {error}")