import numpy as np

print(np.arange(1,10))
print(range(1, 10)) #iterator
print(list(range(1,10))) #list 객체로 반환
print(np.array(range(1,10)))

#1이상 2미만 수 출력. 10간격 jump
print(np.arange(1,2,10))

#arange나 range는 작은 값에서 큰 값으로 진행하기 때문에 아무 값도 안 나오게 됨
print(np.arange(10,1))

#10 이하 1 초과 값 출력. 2간격씩 마이너스
print(np.arange(10,1,-2))