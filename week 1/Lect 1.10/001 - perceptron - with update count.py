import numpy as np

class Perceptron:
    def __init__(self):
        # Initialize weights randomly and count of updates
        self.w = None
        self.update_count = 0

    def convergence(self, X, y):
        """
        Check for convergence of the Perceptron algorithm.
        
        Parameters:
        X : array-like, shape = [n_samples, n_features]
            Input features.
        y : array-like, shape = [n_samples]
            Target values (1 or 0).
            
        Returns:
        bool : True if the algorithm has converged, False otherwise.
        """
        for i in range(len(X)):
            # For positive class (y = 1), check if w.x > 0
            if y[i] == 1 and np.dot(self.w, X[i]) <= 0:
                return False
            # For negative class (y = 0), check if w.x < 0
            if y[i] == 0 and np.dot(self.w, X[i]) >= 0:
                return False
        return True

    def fit(self, X, y):
        """
        Perceptron Learning Algorithm with convergence.
        
        Parameters:
        X : array-like, shape = [n_samples, n_features]
            Input features.
        y : array-like, shape = [n_samples]
            Target values (1 or 0).
            
        Returns:
        self : object
            The fitted model.
        """
        # Initialize weights randomly
        self.w = np.random.rand(X.shape[1])
        
        # Convert labels to -1 (for 0 class) and 1 (for 1 class)
        y_transformed = np.where(y == 0, -1, 1)
        
        # Learning loop
        while not self.convergence(X, y):
            # Pick a random point from the dataset
            for i in range(len(X)):
                # For positive class (y_transformed = 1), if w.x < 0, update w
                if y_transformed[i] == 1 and np.dot(self.w, X[i]) <= 0:
                    self.w = self.w + X[i]
                    self.update_count += 1
                # For negative class (y_transformed = -1), if w.x >= 0, update w
                elif y_transformed[i] == -1 and np.dot(self.w, X[i]) >= 0:
                    self.w = self.w - X[i]
                    self.update_count += 1

        return self

    def predict(self, X):
        """
        Predict class labels for samples in X.
        
        Parameters:
        X : array-like, shape = [n_samples, n_features]
            Input features.
            
        Returns:
        y_pred : array, shape = [n_samples]
            Predicted class labels (1 or 0).
        """
        return np.where(np.dot(X, self.w) > 0, 1, 0)


# Example usage
if __name__ == "__main__":
    # Toy dataset: AND gate logic
    X = np.array([(1,1),(2,3),(4,1),(-1,-1),(-2,-3),(-4,-1)])  # Input features
    y = np.array([1,1,1,0,0,0])  # Output labels
    
    # Create the Perceptron object
    perceptron = Perceptron()

    # Fit the Perceptron model
    perceptron.fit(X, y)
    
    # Output the learned weights and number of updates
    print("Learned weights:", perceptron.w)
    print("Number of weight updates:", perceptron.update_count)
    
    # Make predictions
    predictions = perceptron.predict(X)
    print("Predictions:", predictions)
