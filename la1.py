import numpy as np

B = np.array([[3, -1, -1, 0],
              [-1, 4, 0, -1],
              [-1, 0, 4, -1],
              [0, -1, -1, 3]])

print(np.trace(B)) #대각합을 구하는 함수

print(np.triu(B)) #상삼각행렬 만드는 함수
print(np.tril(B)) #하삼각행렬 만드는 함수

D_vec = np.diag(B) #대각성분 뽑아내기
print(D_vec)
print(np.diag(D_vec)) #대각성분으로 대각행렬 만들기