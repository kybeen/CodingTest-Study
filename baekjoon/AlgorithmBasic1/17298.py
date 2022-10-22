#오큰수

import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(N)]
stk = [0]

for i in range(0,N):
    while stk and sequence[stk[-1]] < sequence[i]:
        result[stk[-1]] = sequence[i]
        stk.pop()
    stk.append(i)

for i in result:
    print(i,end=' ')