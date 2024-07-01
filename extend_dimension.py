import numpy as np

A = np.random.rand(2, 3, 4)
print(A)

print(A.shape)
print(A[:, np.newaxis, :, :].shape) # :은 원래 크기를 순서대로 받아온다. 2, 3, 4를 순서대로 가져온다.
print(A[:, np.newaxis, :, np.newaxis, :].shape)
print(A[:, np.newaxis, :, np.newaxis, :].shape)
print(A[..., np.newaxis].shape) #앞에가 몇개든지 전부 다 포함하고 마지막에 삽입할래 ~
print(A[np.newaxis, ...].shape)