import numpy as np

x = np.array([1, 2, 3])

y = np.array([[1,2],[3,4]])

# repeat는 원소 반복
print(np.repeat(x, 3))
print(np.repeat(y, 3))


# 3차원에서 axis=0은 층, axis=1은 행
# 2차원에서 axis=0은 행, axis=1은 열
print(y)
print(np.repeat(y, 3, axis=0)) # 행으로 반복
print(np.repeat(y, 3, axis=1)) # 열로 반복