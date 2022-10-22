# 연결 요소의 개수 ==> 구글링함.

import sys
# 파이썬의 기본 재귀 깊이 제한이 작기 때문에 대부분의 재귀 문제에서는 이 명령어로 최대 재귀 깊이를 늘려주는게 좋다.
sys.setrecursionlimit(10000)

def dfs(start):
    check[start] = 1
    for i in line[start]:
        if check[i] == 0:
            dfs(i)
    

N, M = map(int, sys.stdin.readline().split())
line = [[] for i in range(N+1)]
# 인접 노드 관계를 line리스트에 저장한다.
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    line[u].append(v)
    line[v].append(u)

check = [0] * (N+1)
result = 1

# 인접 노드 탐색을 한번 수행한 뒤 남은 노드 중에 방문하지 않은 노드가 있다면 연결 요소가 더 있는 것이므로 result를 1 증가시키고 그 노드에 대해서 다시 dfs실행
dfs(1)
for i in range(1,len(check)):
    if check[i] == 0:
        result += 1
        dfs(i)

print(result)