# N과 M(2)

import sys

N, M = map(int, sys.stdin.readline().split())
stk = []

def dfs():
    if len(stk) == M:
        print(' '.join(map(str,stk)))
        return
    for i in range(1,N+1):
        if len(stk) >= 1 and i <= stk[-1]:  # 고른 수열이 오름차순이 되어야 하기 때문에 15649번 문제에서 조건 하나만 바꿈 (i가 스택의 마지막 원소보다 작거나 같을때는 continue)
            continue
        stk.append(i)
        dfs()
        stk.pop()

dfs()