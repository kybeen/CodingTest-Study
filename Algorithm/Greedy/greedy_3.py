# 1이 될 때까지
# 어떤 수 N이 1이 될 때 까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다. (N이 K로 나누어질때만 가능)

import sys

N, K = map(int, sys.stdin.readline().split())
count = 0

while N != 1:
    if N % K == 0:
        N /= K
    else:
        N -= 1
    
    count += 1

print(count)