import numpy as np

# concatenate는 스택과 달리 다른 크기도 쌓음. 내가 갖고 있는 차원에 붙인다. 새로운 차원을 확장하지 않음.
# 붙이는 차원 빼고 다른 차원은 크기가 같아야 함

v1 = np.random.rand(10, 4, 3)
v2 = np.random.rand(20, 4, 3)
v3 = np.random.rand(30, 4, 3)

h1 = np.random.rand(5, 10, 3)
h2 = np.random.rand(5, 20, 3)
h3 = np.random.rand(5, 30, 3)

vstack0 = np.vstack([v1, v2, v3]) # 세로(0차원)에 대해서 concatenate하는 게 vstack. 일반적인 stack과 다르다. concatenate에 가깝다.
concat0 = np.concatenate([v1, v2, v3], axis=0)

hstack1 = np.hstack([h1, h2, h3]) # 가로에 대해서 concatenate하는 게 hstack.
concat1 = np.concatenate([h1, h2, h3], axis=1)

print(vstack0.shape)
print(concat0.shape)
print(hstack1.shape)
print(concat1.shape)
