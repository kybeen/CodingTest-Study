# # 단지번호붙이기

# import sys

# # 인자로 받은 인덱스에서부터 상하좌우에 아파트가 연속해서 위치하는지 탐색한다. 아파트가 위치한다면 그 위치로 다시 dfs함수 재귀실행.
# def dfs(i,j):
#     global danzi, cnt
#     left = j - 1
#     right = j + 1
#     up = i  - 1
#     down = i + 1
#     if left >= 0 and field[i][left] == 1 and visit[i][left] == 0:   # 왼쪽 탐색(i,j-1)
#         visit[i][left] = danzi
#         cnt += 1
#         dfs(i,left)
#     if right < N and field[i][right] == 1 and visit[i][right] == 0: # 오른쪽 탐색(i,j+1)
#         visit[i][right] = danzi
#         cnt += 1
#         dfs(i,right)
#     if up >= 0 and field[up][j] == 1 and visit[up][j] == 0: # 위쪽 탐색(i-1,j)
#         visit[up][j] = danzi
#         cnt += 1
#         dfs(up,j)
#     if down < N and field[down][j] == 1 and visit[down][j] == 0:    # 아래쪽 탐색(i+1,j)
#         visit[down][j] = danzi
#         cnt += 1
#         dfs(down,j)
#     return  # 모든 방향의 탐색이 끝나면 리턴해서 해당 재귀함수를 벗어난다.

# N = int(sys.stdin.readline())
# field = [[] for i in range(N)]
# # 탐색했는지 확인하기 위한 지도 입력받은 지도와 같은 크기, 초기값은 모두 0이고, 탐색하면서 단지 번호로 표시
# visit = [[0 for i in range(N)] for i in range(N)]
# for i in range(N):  # 지도 입력
#     field[i] = list(map(int, sys.stdin.readline().rstrip()))

# danzi = 0   # 아파트 단지 수 카운트
# house_cnt = []  # 단지별 집 개수를 저장할 리스트

# # (0,0)부터 순차적으로 탐색해 나가면서 field값은 1이고(==아파트가 위치한), visit값은 0인(==아직 탐색하지 않음) 인덱스 찾는다.
# for i in range(N):
#     for j in range(N):
#         if field[i][j] == 1 and visit[i][j] == 0:   # 해당하는 인덱스 찾으면 해당 변수들 카운트해주고 dfs 실행
#             cnt = 1
#             danzi += 1
#             visit[i][j] = danzi
#             dfs(i,j)
#             house_cnt.append(cnt)

# print(danzi)
# house_cnt.sort()
# for i in house_cnt:
#     print(i)










# 2022.06.23 풀이
import sys

def dfs(i,j):
    global cnt, danzi_num
    visit[i][j] = 1
    cnt += 1
    up = i - 1
    down = i + 1
    left = j - 1
    right = j + 1
    if i > 0 and visit[up][j] == 0 and zido[up][j] == 1:    # 방문 안했고 지도상에 아파트가 있다면
        dfs(up,j)
    if i < N-1 and visit[down][j] == 0 and zido[down][j] == 1:
        dfs(down,j)
    if j > 0 and visit[i][left] == 0 and zido[i][left] == 1:
        dfs(i,left)
    if j < N-1 and visit[i][right] == 0 and zido[i][right] == 1:
        dfs(i,right)
    
    return cnt

N = int(sys.stdin.readline())
zido = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip()))
    zido.append(temp)

danzi_num = 0
house_num = []
visit = [[0 for i in range(N)] for i in range(N)]

# 지도상에서 아파트가 있으면서 아직 방문하지 않은 좌표가 있으면 그 좌표에서 dfs 시작
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 and zido[i][j] == 1:
            danzi_num += 1
            cnt = 0
            temp = dfs(i,j)
            house_num.append(temp)
print(danzi_num)
house_num.sort()
for i in house_num:
    print(i)