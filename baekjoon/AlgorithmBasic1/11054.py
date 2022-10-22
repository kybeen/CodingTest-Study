# 가장 긴 바이토닉 부분 수열

import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
dp_l = [1] * N
dp_r = [1] * N
result = [0] * N

# 기준 원소 오른쪽의 부분수열의 길이를 구한다.
for i in range(0,N):
    for j in range(0,i):
        if A[j] < A[i]:
            dp_l[i] = max(dp_l[i], dp_l[j]+1)

# 수열을 뒤집어서 기준 원소 오른쪽의 부분수열의 길이를 구한다.
A.reverse()
for i in range(0,N):
    for j in range(0,i):
        if A[j] < A[i]:
            dp_r[i] = max(dp_r[i], dp_r[j]+1)
dp_r.reverse()

for i in range(0,N):
    result[i] = dp_l[i] + dp_r[i] - 1
print(max(result))