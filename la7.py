import numpy as np
#svd
A = np.array([[1, 1],
              [1, 1],
              [-2, 1]])

U, S, VT = np.linalg.svd(A)

print(U)
print(S)
print(VT)