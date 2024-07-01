import numpy as np

arr1 = np.arange(16)
arr2 = arr1.reshape(4, -1)
print(arr2)

print(arr2[1, 3]) #1이 row, 2가 col. 따라서 1행 3열 출력
print(arr2[0, 1])
print(arr2[2, 2])

# 1행 3열, 0행 1열, 2행 2열 출력
print(arr2[[1, 0, 2], [3, 1, 2]])