import numpy as np

np.savez('parameters_w11',U_e=U_e,W_e=W_e,W_d=W_d,U_d=U_d,V_d=V_d)
parameters = np.load(`parameters.npz')
U_e = parameters.get(`U_e')
