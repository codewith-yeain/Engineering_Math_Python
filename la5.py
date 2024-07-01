import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[0, 1, 4],
              [1, 2, 3],
              [5, 6, 0]])

print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(B))