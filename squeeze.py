import numpy as np

A = np.random.rand(2, 1, 4, 1)
print(A)
print(A.shape)

B = A.squeeze() # 크기가 1인 axis 제거
print(B.shape)

C = A.flatten() # A.reshape(-1)과 똑같음. 코드의 가독성을 위해 flatten을 쓰기도 함
print(C.shape)