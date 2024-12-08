import numpy as np

# Input embeddings x
x = np.array([
    [0.1, 0.3, 0.5, 0.2],
    [0.4, 0.1, 0.6, 0.8],
    [0.7, 0.2, 0.9, 0.1],
    [0.5, 0.4, 0.2, 0.6]
])

# Weight matrix W_Q
W_Q = np.array([
    [0.2, 0.3, 0.4, 0.1],
    [0.1, 0.5, 0.6, 0.2]
])

# Calculate Q = x @ W_Q.T
Q = np.dot(x, W_Q.T)

# Calculate the sum of elements of Q
sum_Q = np.sum(Q)
print(sum_Q)


# Weight matrix W_K
W_K = np.array([
    [0.3, 0.1, 0.2, 0.4],
    [0.5, 0.3, 0.1, 0.6]
])

# Calculate K = x @ W_K.T
K = np.dot(x, W_K.T)

# Compute attention scores for the first query vector
query_vector = Q[0]  # First query vector
attention_scores = np.dot(K, query_vector)

# Apply softmax to obtain attention weights
attention_weights = np.exp(attention_scores) / np.sum(np.exp(attention_scores))

# Find the maximum entry in the attention weights
max_attention_weight = np.max(attention_weights)
print(max_attention_weight)


# Weight matrix W_V
W_V = np.array([
    [0.4, 0.2, 0.3, 0.7],
    [0.5, 0.1, 0.2, 0.4]
])

# Calculate V = x @ W_V.T
V = np.dot(x, W_V.T)

# Calculate the context vector for the first query vector
context_vector = np.dot(attention_weights, V)

# Find the maximum entry in the context vector
max_context_entry = np.max(context_vector)
print(max_context_entry)
