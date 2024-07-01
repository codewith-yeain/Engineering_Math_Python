import numpy as np

A = np.array([[2, 0],
              [1, 3]])

w, v = np.linalg.eig(A)

print(w) #고유값
print(v) #고유벡터