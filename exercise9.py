import numpy as np

A = np.array([[2,3,1], [4,5,1]])
B = np.array([[-1,2], [4,2], [3,6]])

AB = np.matmul(A, B)
BA = np.matmul(B, A)

print(A.shape, B.shape)
print(AB.shape, BA.shape)

print(AB)
print(BA)

print("AB=", A @ B)
print("BA=", B @ A) # at(@) 기호. np.matmul(B, A)와 같은 기능의 코드.