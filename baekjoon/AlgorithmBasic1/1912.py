# 연속합 ==> 알고리즘 이해하기 어려웠음. 구글링으로 함

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = [0] + arr
dp = [0] * (n+1)
dp[1] = arr[1]
for i in range(2,n+1):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
print(max(dp[1:]))


#---------> 시간초과
# import sys

# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# arr = [0] + arr
# dp = [0] * (n+1)
# for i in range(1,n+1):
#     dp[i] = temp = arr[i]
#     for j in range(i+1,n+1):
#         temp += arr[j]
#         if temp > dp[i]:
#             dp[i] = temp
# print(max(dp[1:]))