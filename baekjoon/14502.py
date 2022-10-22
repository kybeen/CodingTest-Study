# 연구소
import sys
import collections
import copy

def bfs():
    visited = copy.deepcopy()

    for i in range(N):
        for j in range(M):
            if zido[i][j] == 1:
                visited[i][j] = 1
    dq = collections.deque()
    for i in range(len(virus)):
        dq.append(virus[i])
        visited[virus[i][0]][virus[i][1]]
    
    while dq:
        i, j = dq.popleft()
        up = i-1
        down = i+1
        left = j-1
        right = j+1
        if i > 0 and visited[up][j] == 0 and zido[up][j] == 0:
            dq.append([up,j])
        if i < N-1 and visited[down][j] == 0 and zido[down][j] == 0:
            dq.append([down,j])
        if j > 0 and visited[i][left] == 0 and zido[i][left] == 0:
            dq.append([i,left])
        if j < M-1 and visited[i][right] == 0 and zido[i][right] == 0:
            dq.append([i,right])
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                cnt += 1
    return cnt

N, M = map(int, sys.stdin.readline().split())   # N:세로, M:가로
zido = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    zido.append(temp)

virus = []
for i in range(N):
    for j in range(M):
        if zido[i][j] == 2: # 바이러스 좌표 저장
            virus.append([i,j])
result = []
# 벽 3개를 세우는 경우마다 bfs 수행
trigger = 0
for i in range(N):
    for j in range(M):
        if zido[i][j] == 0:
            trigger += 1
            zido[i][j] = 1
        if trigger == 3:
            temp = bfs()
            result.append(temp)
            zido[i][j] = 0
            trigger -= 1

maximum = max(result)
print(maximum)