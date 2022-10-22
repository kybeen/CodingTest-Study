# N과 M(7)

import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
stk = []

def dfs():
    if len(stk) == M:
        print(' '.join(map(str,stk)))
        return
    for i in num:
        stk.append(i)
        dfs()
        stk.pop()

num.sort()
dfs()