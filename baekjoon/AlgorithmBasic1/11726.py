# 2xn 타일링

import sys

n = int(sys.stdin.readline())
dp = [0]*1001
dp[1], dp[2] = 1, 2
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

result = dp[n] % 10007
print(result)


# dp = [0]*(n+1)로 하니까 런타임 에러
# ==> n의 최댓값 1000까지 dp리스트 만들어놓고 찾는 방식으로 함