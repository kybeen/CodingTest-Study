import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def DFS(x, y):
    # 범위 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해동 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 위치 재귀적으로 호출
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if DFS(i,j) == True:
            result += 1

print(result)