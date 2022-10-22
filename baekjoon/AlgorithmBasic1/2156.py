# 포도주 시식
# ------> dp점화식 만들기 어려웠음, i,i-1번째 마시는 경우 / i, i-2번째 마시는 경우, i-1,i-2번째 마시는 경우 나누기

import sys

n = int(sys.stdin.readline())
drink = [0] * n
for i in range(n):
    drink[i] = int(sys.stdin.readline())

dp = [0] * n
if n >=1:   # n이 3 이하인 경우들 예외처리 안해주면 인덱스 에러 뜸
    dp[0] = drink[0]
if n >= 2:
    dp[1] = drink[0] + drink[1]
if n >= 3:
    dp[2] = max(dp[1], drink[0]+drink[2], drink[1]+drink[2])

for i in range(3,n):
    dp[i] = max(drink[i]+drink[i-1]+dp[i-3], drink[i]+dp[i-2], dp[i-1])
print(dp[-1])