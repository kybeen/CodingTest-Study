# # 토마토

# import sys
# import collections

# def bfs():
#     dq = collections.deque()
#     # 익은 토마토가 있는 자리를 처음에 모두 데크에 저장
#     for i in range(N):
#         for j in range(M):
#             if tomato[i][j] == 1:
#                 dq.append((i,j))
#     while dq:
#         i, j = dq.popleft()
#         left = j - 1
#         right = j + 1
#         up = i - 1
#         down = i + 1
        
#         # 익지 않은 토마토가 있으면 이전 위치의 visit값에서 1 더한 값을 visit에 저장한다.
#         if down < N and tomato[down][j] == 0 and visit[down][j] == 0:
#             visit[down][j] = visit[i][j] + 1
#             dq.append((down,j))
#         if right < M and tomato[i][right] == 0 and visit[i][right] == 0:
#             visit[i][right] = visit[i][j] + 1
#             dq.append((i,right))
#         if up >= 0 and tomato[up][j] == 0 and visit[up][j] == 0:
#             visit[up][j] = visit[i][j] + 1
#             dq.append((up,j))
#         if left >= 0 and tomato[i][left] == 0 and visit[i][left] == 0:
#             visit[i][left] = visit[i][j] + 1
#             dq.append((i,left))
#     return visit

# M, N = map(int, sys.stdin.readline().split())   # M : 가로, N : 세로
# tomato = [[] for i in range(N)]
# for i in range(N):
#     tomato[i] = list(map(int, sys.stdin.readline().split()))

# visit = [item[:] for item in tomato]   # @@2차원 리스트 깊은 복사 하려면 슬라이싱 저렇게 하거나 copy모듈의 deepcopy 사용

# if all(0 not in a for a in tomato): # 처음부터 모든 토마토가 익어 있는 경우
#     print('0')
# else:
#     result = bfs()
#     if all(0 not in a for a in visit):  # visit에 0이 없는 경우(= 익지 않은 토마토가 없는 경우)
#         print(max(map(max, visit)) - 1) # 2차원 리스트에서 최대값 찾기 ==> max(map(max, 리스트))
#     else:   # 익지 않은 토마토가 남아 있는 경우
#         print('-1')








# 2022.06.23
import sys
import collections

# -------- 입력 -----------------------------
M, N = map(int, sys.stdin.readline().split())
tomatoes = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    tomatoes.append(temp)


visit = [[0 for i in range(M)] for i in range(N)]
dq = collections.deque()
for i in range(N):
    for j in range(M):
        # 처음에 익은 토마토가 여러 개 있다면 동시에 시작하기 위해 토마토가 익어 있는 좌표들을 모두 deque에 넣어준다.
        if tomatoes[i][j] == 1:
            dq.append([i,j])
            visit[i][j] = 1
        # 토마토가 들어 있지 않은 칸은 visit에 -1 표시해준다.
        if tomatoes[i][j] == -1:
            visit[i][j] = -1

while dq:
    now = dq.popleft()
    i, j = now[0], now[1]

    up = i - 1
    down = i + 1
    left = j - 1
    right = j + 1
    # 방문하지 않은 자리에 토마토가 익어있지 않다면 deque에 추가한 뒤 현재 위치에서 1 더한 값을 visit에 넣어준다.
    if i > 0 and visit[up][j] == 0 and tomatoes[up][j] == 0:
        dq.append([up,j])
        visit[up][j] = visit[i][j] + 1
    if i < N-1 and visit[down][j] == 0 and tomatoes[down][j] == 0:
        dq.append([down,j])
        visit[down][j] = visit[i][j] + 1
    if j > 0 and visit[i][left] == 0 and tomatoes[i][left] == 0:
        dq.append([i,left])
        visit[i][left] = visit[i][j] + 1
    if j < M-1 and visit[i][right] == 0 and tomatoes[i][right] == 0:
        dq.append([i,right])
        visit[i][right] = visit[i][j] + 1

# 가장 마지막으로 방문한 토마토의 visit값이 가장 크다. (= 토마토가 모두 익기 위한 최소 일수)
temp = []
for row in visit:
    temp.append(max(row))

result = max(temp) - 1  # 맨 처음에 이미 익어있던 토마토의 visit값이 1로 돼있기 때문에 최종결과에서 1을 빼준 수가 실제 걸린 일수임
# 만약 visit에 방문하지 않은 곳이 있다면, 그곳은 토마토가 있는데 익지 못한 것이므로 결과를 -1로 바꿔준다. (토마토가 없는 곳: -1, 익은 토마토: 1, 익지 않은 토마토: 0)
for row in visit:
    if 0 in row:
        result = -1
print(result)