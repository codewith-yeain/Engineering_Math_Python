import numpy as np

A = np.array([[0, 1, 4],
              [1, 2, 3],
              [5, 6, 0]])

Ainv = np.linalg.inv(A) #역행렬 구하기

print(Ainv)