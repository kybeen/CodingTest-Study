# ABCDE ==> 구글링함.

import sys

def dfs(start):
    global result
    stk.append(start)
    check[start] = 1
    if len(stk) == 5:   # stk 길이가 5가 되면 답이 존재 하는 것이므로 result를 1로
        result = 1
        return
    for i in relationship[start]:   # 인접 노드 중에 아직 사용 안한 노드가 있으면 해당 노드를 인자로 받아서 dfs로 재귀
        if check[i] == 0:
            dfs(i)
            stk.pop()
            check[i] = 0

N, M = map(int, sys.stdin.readline().split())
relationship = [[] for i in range(N)]
for i in range(M):  # 입력받은 친구 관계에 따라 인접 노드들을 저장한다.
    a, b = map(int, sys.stdin.readline().split())
    relationship[a].append(b)
    relationship[b].append(a)

stk = []
result = 0  # 답이 존재하면 1, 아니면 0
check = [0] * N

# 시작점이 다른 사람인 경우들 모두 탐색한다.
for i in range(N):
    dfs(i)
    stk.pop()
    check[i] = 0
    if result == 1: # 결과가 존재하면 더이상 탐색하지 않고 break
        break
print(result)