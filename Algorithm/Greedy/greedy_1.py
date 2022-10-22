# 주어진 수들을 M번 더해서 가장 큰 수를 만든다
# 배열의 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음 (같은 인덱스의 수 연속 K번까지만 더할 수 있음)
# 배열의 크기 N, 숫자 더해지는 횟수 M, 연속으로 더할 수 있는 횟수 K

import sys

N, M, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()
max = num_list[-1]

result = 0
enable_K = K

for i in range(M):
    if enable_K != 0:
        result += max
        enable_K -= 1
    else:
        max = num_list[-2]
        result += max
        enable_K = K
        max = num_list[-1]
        

print(result)