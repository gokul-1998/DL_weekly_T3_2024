import numpy as np

x = np.array([
    [0.1, 0.3, 0.5, 0.2],
    [0.4, 0.1, 0.6, 0.8],
    [0.7, 0.2, 0.9, 0.1],
    [0.5, 0.4, 0.2, 0.6]
])
# Corrected weight matrices from the image
W_Q = np.array([
    [0.2, 0.3],
    [0.4, 0.1],
    [0.1, 0.5],
    [0.6, 0.2]
])

W_K = np.array([
    [0.2, 0.4],
    [0.5, 0.3],
    [0.1, 0.6],
    [0.3, 0.1]
])

W_V = np.array([
    [0.4, 0.2],
    [0.3, 0.7],
    [0.5, 0.1],
    [0.2, 0.4]
])

# Recalculate Q, K, and V with corrected W_Q, W_K, and W_V
Q = np.dot(x, W_Q)  # Q = x @ W_Q
K = np.dot(x, W_K)  # K = x @ W_K
V = np.dot(x, W_V)  # V = x @ W_V

# Compute attention scores for the first query vector
query_vector = Q[0]  # First query vector
attention_scores = np.dot(K, query_vector)

# Apply softmax to obtain attention weights
attention_weights = np.exp(attention_scores) / np.sum(np.exp(attention_scores))

# Calculate the context vector for the first query vector
context_vector = np.dot(attention_weights, V)

# Find the maximum entry in the context vector
max_context_entry = np.max(context_vector)
print(max_context_entry)

