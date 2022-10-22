# N과 M(3)

import sys

N, M = map(int, sys.stdin.readline().split())
stk = []

def dfs():
    if len(stk) == M:
        print(' '.join(map(str,stk)))
        return
    for i in range(1,N+1):
        # 같은 수를 여러번 고를 수 있기 때문에 15649번에서 스택에 이미 있는 수는 빼는 조건 없앰
        stk.append(i)
        dfs()
        stk.pop()

dfs()