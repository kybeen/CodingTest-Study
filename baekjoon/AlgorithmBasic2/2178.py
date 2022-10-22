# # 미로 탐색 ==> 구글링함. BFS로 풀어야됨

# import sys
# import collections

# def bfs(start_i,start_j):
#     dq = collections.deque()
#     dq.append((start_i,start_j))    # 데크에 시작 좌표 (0,0)을 넣어준다.

#     while dq:
#         i, j = dq.popleft() # i : row, j : column
#         left = j - 1
#         right = j + 1
#         up = i - 1
#         down = i + 1
        
#         # 각 방향별로 진행 가능한 경우가 있으면 이전 위치에서 1 증가한 값을 넣어준다.(지금까지 거쳐간 칸 수) 그리고 데크에도 해당 좌표를 넣어준다.
#         if down < N and miro[down][j] == '1' and visit[down][j] == 0:
#             visit[down][j] = visit[i][j] + 1    # 이전에 탐색한 위치의 값에서 1 증가한 값을 넣어준다.
#             dq.append((down,j))
#         if right < M and miro[i][right] == '1' and visit[i][right] == 0:
#             visit[i][right] = visit[i][j] + 1
#             dq.append((i,right))
#         if up >= 0 and miro[up][j] == '1' and visit[up][j] == 0:
#             visit[up][j] = visit[i][j] + 1
#             dq.append((up,j))
#         if left >= 0 and miro[i][left] == '1' and visit[i][left] == 0:
#             visit[i][left] = visit[i][j] + 1
#             dq.append((i,left))
    
#     return visit[N-1][M-1]  # 진행 가능한 모든 좌표의 탐색이 끝났으면 (N-1,M-1)좌표에서의 거쳐간 칸 수를 리턴


# N, M = map(int, sys.stdin.readline().split())
# miro = [[] for i in range(N)]
# for i in range(N):
#     miro[i] = list(sys.stdin.readline().rstrip())
# visit = [[0 for i in range(M)] for i in range(N)]   # 방문 여부를 확인하기 위한 미로와 같은 크기의 리스트
# visit[0][0] = 1 # 시작 위치는 방문한걸로 고정

# result = bfs(0,0)
# print(result)


# ---------------------------------> [DFS풀이] 답은 맞는것 같은데 시간초과 뜸. 구글링해보니까 최단 경로 문제는 BFS로 푸는게 더 낫다. DFS는 최단 경로라는 보장이 없음.
# import sys
# sys.setrecursionlimit(10 ** 6)

# def dfs(i,j):
#     global cnt, result
#     if i == N-1 and j == M-1:   # (N,M)위치로 오게 되면 cnt 출력
#         result = min(result, cnt)
#         return
#     left = j-1
#     right = j+1
#     up = i-1
#     down = i+1
#     if right < M and visit[i][right] == 0 and miro[i][right] == '1':
#         visit[i][right] = 1
#         cnt += 1
#         dfs(i,right)
#         # 더 가지 못하고 재귀함수에서 빠져나와서 돌아오게 되면 cnt를 감소시켜주고, visit표시도 없앤다
#         visit[i][right] = 0
#         cnt -= 1
#     if down < N and visit[down][j] == 0 and miro[down][j] == '1':
#         visit[down][j] = 1
#         cnt += 1
#         dfs(down,j)
#         visit[down][j] = 0
#         cnt -= 1
#     if up >= 0 and visit[up][j] == 0 and miro[up][j] == '1':
#         visit[up][j] = 1
#         cnt += 1
#         dfs(up,j)
#         visit[up][j] = 0
#         cnt -= 1
#     if left >= 0 and visit[i][left] == 0 and miro[i][left] == '1':
#         visit[i][left] = 1
#         cnt += 1
#         dfs(i,left)
#         visit[i][left] = 0
#         cnt -= 1
#     return

# N, M = map(int, sys.stdin.readline().split())
# miro = [[] for i in range(N)]
# for i in range(N):
#     miro[i] = list(sys.stdin.readline().rstrip())
# visit = [[0 for i in range(M)] for i in range(N)]   # 방문 여부를 확인하기 위한 미로와 같은 크기의 리스트
# visit[0][0] = 1 # 시작 위치는 방문한걸로 고정
# cnt = 1
# result = sys.maxsize

# dfs(0,0)
# print(result)










# 2022.06.23 풀이 - BFS
import sys
import collections

N, M = map(int, sys.stdin.readline().split())
miro = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    miro.append(temp)

visit = [[0 for i in range(M)] for i in range(N)]
dq = collections.deque()
dq.append([0,0])
visit[0][0] = 1 # 시작점 방문 표시

while dq:
    now = dq.popleft()
    i, j = now[0], now[1]
    up = i - 1
    down = i + 1
    left = j - 1
    right = j + 1
    
    if i > 0 and miro[up][j] == 1 and visit[up][j] == 0:
        dq.append([up,j])
        visit[up][j] = visit[i][j] + 1
    if i < N-1 and miro[down][j] == 1 and visit[down][j] == 0:
        dq.append([down,j])
        visit[down][j] = visit[i][j] + 1
    if j > 0 and miro[i][left] == 1 and visit[i][left] == 0:
        dq.append([i,left])
        visit[i][left] = visit[i][j] + 1
    if j < M-1 and miro[i][right] == 1 and visit[i][right] == 0:
        dq.append([i,right])
        visit[i][right] = visit[i][j] + 1
print(visit[N-1][M-1])