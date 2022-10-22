# 2xn 타일링2 --> 11726번 문제에서
# dp[i] = dp[i-1] + dp[i-2] =====> dp[i] = dp[i-1] + 2*dp[i-2] 조건 추가
# i-2일때 (1x2)타일로 추가하는 경우의 수랑 (2x2)타일로 추가하는 경우의 수가 같기 때문에
# dp[1[ = 1, dp[2] = 3으로 시작

import sys

n = int(sys.stdin.readline())
dp = [0]*1001
dp[1], dp[2] = 1, 3
for i in range(3,n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]

result = dp[n] % 10007
print(result)