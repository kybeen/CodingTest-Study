# N과 M(4)

import sys

N, M = map(int, sys.stdin.readline().split())
stk = []

def dfs():
    if len(stk) == M:
        print(' '.join(map(str,stk)))
        return
    for i in range(1,N+1):
        if len(stk) >= 1 and i < stk[-1]:   # 고른 수열이 비내림차순이 되게 하기 위해 15650 문제의 조건 i <= stk[-1]을 <로 바꿈
            continue
        stk.append(i)
        dfs()
        stk.pop()

dfs()