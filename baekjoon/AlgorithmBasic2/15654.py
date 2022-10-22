# N과 M(5)

import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
stk = []

def dfs():
    if len(stk) == M:
        print(' '.join(map(str,stk)))
        return
    for i in num:
        if i in stk:    # i를 입력받은 num리스트에서 탐색하는것 빼고는 15649번과 동일
            continue
        stk.append(i)
        dfs()
        stk.pop()

num.sort()  # 처음에 입력받은 숫자들을 오름차순으로 탐색하기 위해 정렬한다.
dfs()