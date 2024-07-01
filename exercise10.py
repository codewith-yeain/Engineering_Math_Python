import numpy as np

A = np.array([[1,3], [2,-1]])
I = np.eye(2)

print(A @ I)
print(I @ A)