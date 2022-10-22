# 테트로미노

import sys

N, M = map(int,sys.stdin.readline().split())
num = [0] * N
for i in range(N):
    num[i] = list(map(int,sys.stdin.readline().split()))

result = 0
for i in range(0,N):
    for j in range(0,M):
        if j < M-3: # 가로4칸인 모양
            result = max(result, num[i][j] + num[i][j+1] + num[i][j+2] + num[i][j+3])
        if i < N-3: # 세로4칸인 모양
            result = max(result, num[i][j] + num[i+1][j] + num[i+2][j] + num[i+3][j])
        if i < N-1 and j < M-1: # 가로2칸 세로2칸인 모양
            result = max(result, num[i][j] + num[i][j+1] + num[i+1][j] + num[i+1][j+1])
        if i < N-2 and j < M-1: # 가로2칸 세로3칸인 모양
            result = max(result, num[i][j] + num[i+1][j] + num[i+2][j] + num[i+2][j+1])
            result = max(result, num[i][j] + num[i][j+1] + num[i+1][j+1] + num[i+2][j+1])
            result = max(result, num[i][j+1] + num[i+1][j+1] + num[i+2][j] + num[i+2][j+1])
            result = max(result, num[i][j] + num[i][j+1] + num[i+1][j] + num[i+2][j])
            result = max(result, num[i][j+1] + num[i+1][j] + num[i+1][j+1] + num[i+2][j+1])
            result = max(result, num[i][j] + num[i+1][j] + num[i+1][j+1] + num[i+2][j+1])
            result = max(result, num[i][j+1] + num[i+1][j] + num[i+1][j+1] + num[i+2][j])
            result = max(result, num[i][j] + num[i+1][j] + num[i+1][j+1] + num[i+2][j])
        if i < N-1 and j < M-2: # 가로3칸 세로2칸인 모양
            result = max(result, num[i][j] + num[i][j+1] + num[i][j+2] + num[i+1][j+1])
            result = max(result, num[i][j+1] + num[i+1][j] + num[i+1][j+1] + num[i+1][j+2])
            result = max(result, num[i][j] + num[i][j+1] + num[i+1][j+1] + num[i+1][j+2])
            result = max(result, num[i][j+1] + num[i][j+2] + num[i+1][j] + num[i+1][j+1])
            result = max(result, num[i][j] + num[i+1][j] + num[i+1][j+1] + num[i+1][j+2])
            result = max(result, num[i][j+2] + num[i+1][j] + num[i+1][j+1] + num[i+1][j+2])
            result = max(result, num[i][j] + num[i][j+1] + num[i][j+2] + num[i+1][j+2])
            result = max(result, num[i][j] + num[i][j+1] + num[i][j+2] + num[i+1][j])
print(result)