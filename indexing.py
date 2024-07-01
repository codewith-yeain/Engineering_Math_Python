import numpy as np

arr1 = np.arange(12)
arr2 = arr1.reshape(2, -1)
print(arr1)
print(arr2)

print(arr1[0])

print(arr2[0]) # 이거보다는
print(arr2[0, :]) # 이 방법이 좋음

print(arr2[0, 0])