# 섬의 개수

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(i,j):
    global result
    left = j - 1
    right = j + 1
    up = i - 1
    down = i + 1
    # 왼쪽
    if left >= 0 and field[i][left] == 1 and visit[i][left] == 0:
        visit[i][left] = 1
        dfs(i,left)
    # 오른쪽
    if right < w and field[i][right] == 1 and visit[i][right] == 0:
        visit[i][right] = 1
        dfs(i,right)
    # 위
    if up >= 0 and field[up][j] == 1 and visit[up][j] == 0:
        visit[up][j] = 1
        dfs(up,j)
    # 아래
    if down < h and field[down][j] == 1 and visit[down][j] == 0:
        visit[down][j] = 1
        dfs(down,j)
    # 왼쪽위
    if left >= 0 and up >= 0 and field[up][left] == 1 and visit[up][left] == 0:
        visit[up][left] = 1
        dfs(up,left)
    # 오른쪽위
    if right < w and up >= 0 and field[up][right] == 1 and visit[up][right] == 0:
        visit[up][right] = 1
        dfs(up,right)
    # 왼쪽아래
    if left >= 0 and down < h and field[down][left] == 1 and visit[down][left] == 0:
        visit[down][left] = 1
        dfs(down,left)
    # 오른쪽아래
    if right < w and down < h and field[down][right] == 1 and visit[down][right] == 0:
        visit[down][right] = 1
        dfs(down,right)
    return

while True:
    w, h = map(int, sys.stdin.readline().split())   # w : 지도 너비, h : 지도 높이
    if w == 0 and h == 0:
        break
    result = 0
    field = [[] for i in range(h)]
    visit = [[0 for i in range(w)] for i in range(h)]
    for i in range(h):
        field[i] = list(map(int, sys.stdin.readline().split()))
    
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1 and visit[i][j] == 0:
                visit[i][j] == 1
                dfs(i,j)
                result += 1
    print(result)