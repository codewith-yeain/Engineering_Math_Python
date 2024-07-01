import numpy as np

# 같은 크기의 배열을 모아서 새로운 차원으로 확장하는 게 스택(아니면 concatenate)
a1 = np.random.rand(5, 100)
a2 = np.random.rand(5, 100)
a3 = np.random.rand(5, 100)

a_stack = np.stack([a1, a2, a3])
a_stack_0 = np.stack([a1, a2, a3], axis=0) # 맨 앞쪽에 쌓아줘(중요)

a_stack_1 = np.stack([a1, a2, a3], axis=1)

a_stack_2 = np.stack([a1, a2, a3], axis=2)
a_stack_m = np.stack([a1, a2, a3], axis=-1) # 맨 뒤쪽에 쌓아줘(중요)

print(a_stack.shape)
print(a_stack_0.shape)
print(a_stack_1.shape)
print(a_stack_2.shape)
print(a_stack_m.shape)

