import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_function
        self.weights = None
        self.bias = None

    def _unit_step_function(self, x):
        return np.where(x >= 0, 1, 0)

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0

        # training
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)

                # Perceptron update rule
                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted


# Example usage
if __name__ == "__main__":
    # Toy dataset: AND gate logic
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input features
    y = np.array([0, 0, 0, 1])  # Output labels (AND gate)

    # Initialize the perceptron
    p = Perceptron(learning_rate=0.1, n_iters=1000)
    
    # Train the perceptron
    p.fit(X, y)
    
    # Predict the outputs
    predictions = p.predict(X)
    print("Predicted outputs:", predictions)
