# 오르막 수

import sys

N = int(sys.stdin.readline())
dp = [[1]*10 for i in range(N)]

for i in range(1,N):
    k = 1
    while k <= 9:
        temp = 0
        for j in range(0,k+1):
            temp += dp[i-1][j]
        dp[i][k] = temp
        k += 1
result = sum(dp[N-1]) % 10007
print(result)



# --------------------------> 파이썬에서 sum은 예약어니 절대절대절대 변수로 쓰지 말것
# import sys

# N = int(sys.stdin.readline())
# dp = [[1]*10 for i in range(N)]

# for i in range(1,N):
#     k, j, sum = 1, 0, 0
#     while j <= k and k <= 9:
#         sum += dp[i-1][j]
#         j += 1
#     dp[i][k] = sum
#     k += 1

# print(sum(dp[N-1]))