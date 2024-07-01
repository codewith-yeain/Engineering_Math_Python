import numpy as np

X = np.array([1, 2, 3])

# 2*2 배열
Y = np.array([[1, 2],
              [3, 4]])

print(np.repeat(X, 3))
print(np.tile(X, 3))

print(np.tile(Y, [1, 1]))
print(np.tile(Y, [2, 1])) # 행에 대해 2개 쌓임
print(np.tile(Y, [1, 3])) # 열에 대해 3개 쌓임
print(np.tile(Y, [2, 4])) # 행에 대해 2개, 열에 대해 4개 쌓임