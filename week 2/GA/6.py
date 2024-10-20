

import numpy as np

# Sigmoid function
def sigmoid(x, w, b):
    return 1 / (1 + np.exp(-(w * x + b)))

# Gradient of the sigmoid function with respect to w and b
def gradients(x, y, w, b):
    y_pred = sigmoid(x, w, b)
    error = y_pred - y
    # is it alwas pred - y? 
    # 
    grad_w = error * x
    grad_b = error
    return grad_w, grad_b

# Gradient descent function
def gradient_descent(x, y, w, b, lr, num_iterations):
    w_values = [w]
    b_values = [b]
    
    for _ in range(num_iterations):
        dw_total, db_total = 0, 0
        
        for xi, yi in zip(x, y):
            grad_w, grad_b = gradients(xi, yi, w, b)
            dw_total += grad_w
            db_total += grad_b
        
        # Update weights and biases
        w -= lr * dw_total / len(x)
        b -= lr * db_total / len(x)
        
        w_values.append(w)
        b_values.append(b)
    
    return w_values, b_values

# Dataset
x = np.array([-1, 0.2])
y = np.array([0.5, 0.97])

# Initial parameters
w_init = 2
b_init = 2

# Learning rate and number of iterations
learning_rate = 0.1
iterations = 3

# Run gradient descent
w_sequence, b_sequence = gradient_descent(x, y, w_init, b_init, learning_rate, iterations)

print(w_sequence, b_sequence)

# https://discourse.onlinedegree.iitm.ac.in/t/week-2-graded-ques-6/76825