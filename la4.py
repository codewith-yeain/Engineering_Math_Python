import numpy as np

A1 = np.array([[3, 2], # O
               [2, 1]])
b1 = np.array([5, 4]) # O

A2 = np.array([[0, 1, 4],
               [1, 2, 3],
               [5, 6, 0]])
b2 = np.array([2, -3, 5])

A1inv = np.linalg.inv(A1) # O
A2inv = np.linalg.inv(A2)

x1 = A1inv @ b1 # O
x2 = A2inv @ b2

print(x1) # O
print(x2)