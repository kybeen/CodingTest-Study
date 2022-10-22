# KT AIVLE SCHOOL 코딩테스트 2번 문제

# # ----- [ DFS - 어케푸노 시팔 ] -----
# def solution(house, roadmap, mon):
#     answer = 0
#     company = []    # 회사의 위치
#     roadmap2 = [[1 for i in range(len(roadmap[0]))] for i in range(len(roadmap))]    # 지도 리스트로 다시 생성 (1: 가능한 길 0: 불가능한 길)
#     for i in range(len(roadmap)):
#         for j in range(len(roadmap[i])):
#             if roadmap[i][j] == 'O':
#                 company = [i, j]
#             if roadmap[i][j] == 'X':
#                 roadmap2[i][j] = 0
#     # for row in roadmap:
#     #     print(row)
#     # for row in visited:
#     #     print(row)

#     visited = [[0 for i in range(len(roadmap[0]))] for i in range(len(roadmap))]
#     distance = []
#     for house_num in range(len(house)):
#         i, j = house[house_num][0], house[house_num][1]
#         new_visited = visited
#         temp = dfs(roadmap2, i, j, company, new_visited, house_num, [])
#         print(temp)
#     return answer

# def dfs(roadmap2, i, j, company, visited, house_num, result):
#     visited[i][j] = 1
#     if i == company[0] and j == company[1]: # 회사에 도착하면 리턴
#         case_sum = 0
#         for row in range(len(visited)):
#             case_sum += sum(visited[row])
#         result.append(case_sum)
#         return result
#     else:
#         left = j-1
#         right = j+1
#         up = i-1
#         down = i+1
#         if j > 0 and roadmap2[i][left] == 1 and visited[i][left] == 0: # 왼쪽 탐색
#             visited[i][left] = 1
#             dfs(roadmap2, i, left, company, visited, house_num, result)
#             visited[i][left] = 0
#         if j < len(roadmap2[0])-1 and roadmap2[i][right] == 1 and visited[i][right] == 0:   # 오른쪽 탐색
#             visited[i][right] = 1
#             dfs(roadmap2, i, right, company, visited, house_num, result)
#             visited[i][right] = 0
#         if i > 0 and roadmap2[up][j] == 1 and visited[up][j] == 0:  # 위쪽 탐색
#             visited[up][j] = 1
#             dfs(roadmap2, up, j, company, visited, house_num, result)
#             visited[up][j] = 0
#         if i < len(roadmap2)-1 and roadmap2[down][j] == 1 and visited[down][j] == 0:    # 아래쪽 탐색
#             visited[down][j] = 1
#             dfs(roadmap2, down, j, company, visited, house_num, result)
#             visited[down][j] = 0
#         return result

# house = [
#     [0, 9, 100],
#     [2, 8, 200],
#     [3, 2, 1],
#     [5, 0, 47]
# ]
# roadmap = [
#     ".........H",
#     "..........",
#     ".XXXXXXXH.",
#     ".XH....X..",
#     ".XXXXX.X..",
#     "H......X.O",
# ]
# mon = 3

# result = solution(house, roadmap, mon)




# ----- [ BFS ] -----
import collections

def solution(house, roadmap, mon):
    answer = 0
    roadmap2 = [[1 for i in range(len(roadmap[0]))] for i in range(len(roadmap))]   # 갈 수 있는 길과 없는 길로만 구분한 지도로 다시 만들어준다.
    for i in range(len(roadmap)):
        for j in range(len(roadmap[0])):
            if roadmap[i][j] == 'X':    # 갈 수 없는 길은 0으로 표시해준다
                roadmap2[i][j] = 0
            if roadmap[i][j] == 'O':
                company = [i,j] # 회사의 좌표
    
    shortest_path = []  # 각 집의 최단거리를 저장할 리스트
    for home in house:  # 각 집마다 최단거리 구하기 (BFS)
        start = [home[0], home[1]]  # 시작 좌표 -> 집의 좌표
        dq = collections.deque()
        dq.append(start)    # 시작 좌표를 deque에 넣어준다.
        visited = [[0 for i in range(len(roadmap[0]))] for i in range(len(roadmap))]
        visited[start[0]][start[1]] = 1   # 시작 집 방문 표시
        while dq:
            now = dq.popleft()
            i, j = now[0], now[1]
            
            up = i-1
            down = i+1
            left = j-1
            right = j+1
            if i > 0 and visited[up][j] == 0 and roadmap2[up][j] == 1:
                visited[up][j] = visited[i][j] + 1
                dq.append([up,j])
            if i < len(roadmap2)-1 and visited[down][j] == 0 and roadmap2[down][j] == 1:
                visited[down][j] = visited[i][j] + 1
                dq.append([down,j])
            if j > 0 and visited[i][left] == 0 and roadmap2[i][left] == 1:
                visited[i][left] = visited[i][j] + 1
                dq.append([i,left])
            if j < len(roadmap2[0])-1 and visited[i][right] == 0 and roadmap2[i][right] == 1:
                visited[i][right] = visited[i][j] + 1
                dq.append([i,right])
        shortest_path.append(visited[company[0]][company[1]] - 1)   # 회사 좌표의 visit값 - 1을 최단거리 리스트에 넣어준다. (시작 지점에서 1로 시작했기 때문에 1을 빼줌)

    cost = [] # 각 집의 총 비용을 저장할 리스트
    for i in range(len(house)):
        traffic_cost = shortest_path[i] // 5 * 23 * mon
        home_cost = house[i][2] * mon
        total_cost = traffic_cost + home_cost
        cost.append(total_cost)
    minimum = min(cost)
    answer = cost.index(minimum) + 1
    return answer



house = [
    [0, 9, 100],
    [2, 8, 200],
    [3, 2, 1],
    [5, 0, 47]
]
roadmap = [
    ".........H",
    "..........",
    ".XXXXXXXH.",
    ".XH....X..",
    ".XXXXX.X..",
    "H......X.O",
]
mon = 3

result = solution(house, roadmap, mon)
print(result)