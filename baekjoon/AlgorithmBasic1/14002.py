# 가장 긴 증가하는 부분 수열4
# ==> 11053과 똑같이 한 후, max(dp)값과 dp배열의 원소를 끝에서부터 비교해가며 같은 경우 해당 인덱스의 수열에서의 원소를 결과 리스트에 추가한다.

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1)
temp = max(dp)
print(temp)

result = []
for i in range(-1,-(N+1),-1):
    if dp[i] == temp:
        result.append(A[i])
        temp -= 1
result.reverse()
print(' '.join(map(str,result)))