import numpy as np

# Load parameters
parameters = np.load("/home/gokul/gokul_repos/DL_weekly_T3_2024/dl_t3_2024/app/week 11/GA/parameters_w11.npz")
U_e = parameters["U_e"]
W_e = parameters["W_e"]
W_d = parameters["W_d"]
U_d = parameters["U_d"]
V = parameters["V_d"]

# Check parameter shapes
assert U_e.shape == (5, 5), "U_e shape mismatch"
assert W_e.shape == (5, 5), "W_e shape mismatch"
assert W_d.shape == (5, 5), "W_d shape mismatch"
assert U_d.shape == (5, 5), "U_d shape mismatch"
assert V.shape == (5, 5), "V shape mismatch"

# One-hot encoded input and target sequences
x_source = np.array([
    [1, 0, 0, 0, 0],  # 'a'
    [0, 1, 0, 0, 0],  # 'r'
    [0, 0, 1, 0, 0],  # 'i'
    [0, 0, 0, 1, 0],  # 'y'
    [0, 0, 0, 0, 1]   # 'a'
]).T  # Shape: (5, 5)

x_target = np.array([
    [1, 0, 0, 0, 0],  # 'l'
    [0, 1, 0, 0, 0],  # 'e'
    [0, 0, 1, 0, 0],  # 'a'
    [0, 0, 0, 1, 0],  # 'r'
    [0, 0, 0, 0, 1]   # 'n'
]).T

# Initialize hidden states
h = np.zeros((5, x_source.shape[1]))   # Encoder hidden states
s = np.zeros((5, x_target.shape[1]))   # Decoder hidden states
y_hat = np.zeros((5, x_target.shape[1])) # Predicted output probabilities

# Softmax function
def softmax(x):
    e_x = np.exp(x - np.max(x))  
    return e_x / e_x.sum(axis=0)

# Encoder: Compute h_t
for t in range(x_source.shape[1]):  
    h[:, t] = np.tanh(U_e @ x_source[:, t] + (W_e @ h[:, t - 1] if t > 0 else np.zeros(5)))

# Decoder: Compute s_t and y_hat
s[:, 0] = h[:, -1]  
for t in range(1, x_target.shape[1]):
    s[:, t] = np.tanh(U_d @ x_target[:, t - 1] + W_d @ s[:, t - 1])
    y_hat[:, t] = softmax(V @ s[:, t])

# Ensure y_hat is computed for all timesteps
y_hat[:, 0] = softmax(V @ s[:, 0])  

# Loss computation
loss = -np.sum(x_target * np.log(y_hat + 1e-8))  
print(f"Total Loss L(θ): {loss}")