

inputs=[(1,1),(2,3),(4,1),(-1,-1),(-2,-3),(-4,-1)]
outputs=[1,1,1,0,0,0]


import numpy as np

import numpy as np

def convergence(X, y, w):
    """
    Check for convergence of the Perceptron algorithm.
    
    Parameters:
    X : array-like, shape = [n_samples, n_features]
        Input features.
    y : array-like, shape = [n_samples]
        Target values (1 or 0).
    w : array-like, shape = [n_features]
        Current weights.
        
    Returns:
    bool : True if the algorithm has converged, False otherwise.
    """
    for i in range(len(X)):
        # For positive class (y = 1), check if w.x > 0
        if y[i] == 1 and np.dot(w, X[i]) <= 0:
            return False
        # For negative class (y = 0), check if w.x < 0
        if y[i] == 0 and np.dot(w, X[i]) >= 0:
            return False
    return True

def perceptron_learning_algorithm(X, y):
    """
    Perceptron Learning Algorithm with convergence.
    
    Parameters:
    X : array-like, shape = [n_samples, n_features]
        Input features.
    y : array-like, shape = [n_samples]
        Target values (1 or 0).
        
    Returns:
    w : array-like, shape = [n_features]
        Learned weights.
    """
    
    # Initialize weights randomly
    w = np.random.rand(X.shape[1])
    
    # Convert labels to -1 (for 0 class) and 1 (for 1 class)
    y_transformed = np.where(y == 0, -1, 1)
    
    # Learning loop
    while not convergence(X, y, w):
        # Pick a random point from the dataset
        for i in range(len(X)):
            # For positive class (y_transformed = 1), if w.x < 0, update w
            if y_transformed[i] == 1 and np.dot(w, X[i]) <= 0:
                w = w + X[i]
            # For negative class (y_transformed = -1), if w.x >= 0, update w
            elif y_transformed[i] == -1 and np.dot(w, X[i]) >= 0:
                w = w - X[i]

    return w

# Example usage
if __name__ == "__main__":
    # Toy dataset: AND gate logic
    X = np.array([(1,1),(2,3),(4,1),(-1,-1),(-2,-3),(-4,-1)])  # Input features
    y = np.array([1,1,1,0,0,0])  

    # Run the Perceptron Learning Algorithm
    weights = perceptron_learning_algorithm(X, y)
    print("Learned weights:", weights)
    print("Predictions:", np.where(np.dot(X, weights) > 0, 1, 0))
