import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr + 4)
print(arr - 4)
print(arr * 4)

print(arr / 4)
print(arr // 4)
print(arr % 4)
print(arr * 4)


arr1 = np.array([1,2,3,4,5,6,7,8,9])
arr2 = np.array([2,2,2,2,2,2,2,2,2])

print(arr1)
print(arr2)

print(arr1 + arr2)
np.add(arr1, arr2) # 더하기라는 기호에다가 add라는 함수를 매핑시키는 이러한 기능을 연산자 오버로딩이라고 함.

print(arr1 - arr2)
np.subtract(arr1, arr2)

print(arr1 * arr2)


print(arr1 / arr2)
print(arr1 // arr2)
print(arr1 % arr2)
print(arr2 ** arr1)