#1로 만들기

import sys

N = int(sys.stdin.readline())
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 #1을 뺐을 경우 먼저 dp리스트에 추가

    if i % 2 == 0:  #만약 i가 2로 나눠지는 수면
        dp[i] = min(dp[i], dp[i//2]+1)  #1을 뺀 경우와 2로 나눈 경우에서 최솟값을 저장
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)  #i가 3으로 나눠지는 경우도 똑같이---> 2와 3둘 다로도 나누어지는 수일 수도 있기 때문에 elif 말고 if

print(dp[-1])