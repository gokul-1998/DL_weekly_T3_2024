import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-(20*x+1)))

points=[(0.06,0.4),(0.4,0.95)]

def squared_error(y,y_pred):
    return (y-y_pred)**2

def  mse():
    error=0
    for point in points:
        x,y=point
        y_pred=sigmoid(x)
        error+=squared_error(y,y_pred)
    return error/len(points)

print(mse())