import numpy as np

arr = np.arange(16).reshape(4, 4)

print(arr)
print(arr[1:3, 1:3])
print(arr[:, :])
print(arr[1:, :-1])