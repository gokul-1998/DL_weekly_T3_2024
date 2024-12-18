import numpy as np

# Input matrix X (embeddings as columns)
X = np.array([
    [1, 0, 1],  # First row of embeddings
    [0, 1, 1]   # Second row of embeddings
])

# Transformation matrices
W_q = np.array([
    [1, 0],
    [0, 1]
])

W_k = np.array([
    [0, 1],
    [1, 0]
])

W_v = np.array([
    [1, 0],
    [1, 1]
])

# Compute Q, K, V matrices
Q = W_q @ X
K = W_k @ X
V = W_v @ X

# Value vector of the third word ("sat")
v_third_word = V[:, 2]

# Sum of values in the value vector of the third word
v_sum_third_word = v_third_word.sum()
print(Q,"q\n" ,K,"k\n", V,'v\n', v_third_word,'sds\n', v_sum_third_word)
