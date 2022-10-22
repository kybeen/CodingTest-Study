#오등큰수

import sys
from collections import Counter

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
result = [-1 for _ in range(N)]
stk = [0]
count = dict(Counter(sequence))

for i in range(0,N):
    while stk and count[sequence[stk[-1]]] < count[sequence[i]]:
        result[stk[-1]] = sequence[i]
        stk.pop()
    stk.append(i)

for i in result:
    print(i,end=' ')