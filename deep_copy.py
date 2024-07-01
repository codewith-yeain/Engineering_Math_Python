import numpy as np

# shallow copy
arr1 = np.arange(12)
arr2 = arr1.reshape(2, -1)
arr3 = arr1[2:10]


# deep copy
arr4 = arr2.copy() #전체 copy. 

arr2[0, 0] = 10
#arr1과 arr2가 메모리를 공유하고 있기 때문에 arr2에서만 값을 바꿔도 arr1에 적용됨

print(arr1)
print(arr2)
print(arr3)
print(arr4) #copy는 값만 복사를 해오지, 메모리를 공유하지는 않는다.