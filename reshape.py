import numpy as np

arr1 = np.arange(16)
# 1차원 배열을 2차원으로 바꾸고 싶을 때
arr2 = np.reshape(arr1, (4,4))

arr1 = np.arange(16)
arr2 = arr1.reshape(4,4)
print(arr1)
print(arr2)


arr1 = np.arange(8)
print(arr1)

# 2행. -1은 열을 알아서 하라는 의미
arr2 = np.reshape(arr1, (2, -1))
print(arr2)

# 4열. -1은 행을 알아서 하라는 의미
arr3 = np.reshape(arr1, (-1, 4))
print(arr3)

# n차원을 1차원으로 펼치고 싶을 때
arr4 = np.reshape(arr3, (-1))
print(arr4)

# arr5 = np.reshape(arr1, (-1, 3))
# print(arr5)
