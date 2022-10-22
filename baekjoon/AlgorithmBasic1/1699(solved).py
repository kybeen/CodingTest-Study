# 제곱수의 합 ---> 시간초과

#------> 구글링한 코든데 시간초과 나옴; ===> pypy3에서는 맞다고 뜸
import sys
import math

N = int(sys.stdin.readline())
dp = [0]*(N+1)

for i in range(1,N+1):
    dp[i] = i
    for j in range(1,int(math.sqrt(i)+1)):
        dp[i] = min(dp[i], dp[i-j*j]+1)
print(dp[N])




# -------------------> 결과는 나오는데 시간초과
# import sys
# import math

# N = int(sys.stdin.readline())
# rng = int(math.sqrt(N))
# square = [0]*(rng+1)
# for i in range(1,rng+1):
#     square[i] = i**2

# num = 0
# i = -1
# while N != 0:
#     if(square[i] == square[0]):
#         N -= 1
#         num += 1
#     else:
#         N -= square[i]
#         i -= 1
#         num += 1

# print(num)