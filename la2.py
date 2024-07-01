import numpy as np

B = np.array([[3, -1, -1, 0],
              [-1, 4, 0, -1],
              [-1, 0, 4, -1],
              [0, -1, -1, 3]])

detB = np.linalg.det(B) #행렬식 구하기

print("Determinant of B=", detB)