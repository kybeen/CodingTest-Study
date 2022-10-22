#소인수분해

import sys

N = int(sys.stdin.readline())
k = 2
result = []
while N != 1:
    if N % k == 0:
        N = N / k
        result.append(k)
    else:
        k += 1

for i in result:
    print(i,'\n'.rstrip())