# 외판원 순회2 ==> 구글코드 베낌, 어려웠음. 다시보기@@

import sys

# 매개변수 -> 출발점, 현재위치 , 현재까지의cost
def dfs(start, current, current_cost):
    global result
    
    if current_cost > result:   # current_cost가 result보다 커지면 더이상 확인할 필요가 없으므로 바로 리턴한다.
        return
    if visited.count(1) == N-1:  # 모든 도시를 방문하게 되면(시작 도시는 visited체크를 안했기 때문에 N-1)
        if cost[current][start] != 0:   # 마지막으로 방문한 도시에서 첫번째 도시로 가는 길이 있으면
            result = min(result, current_cost+cost[current][start])  # current_cost에 마지막 도시에서 첫번째 도시로 가는 비용까지 더해준 후, result와 비교하여 더 작은 값으로 갱신
        return

    for i in range(N):
        if cost[current][i] != 0 and i != start and visited[i] == 0:    # 가는 길이 존재하는지, 다음 도시가 시작점이 아닌지, 방문한 적이 있는지 없는지를 모두 검사해서 가능한 도시로 넘어간다.
            visited[i] = 1
            dfs(start, i, current_cost+cost[current][i])    # 현재위치와 현재까지 비용을 갱신하여 함수를 재귀한다.
            visited[i] = 0

N = int(sys.stdin.readline())
cost = [0] * N
for i in range(N):
    cost[i] = list(map(int, sys.stdin.readline().split()))

result = sys.maxsize    # min함수로 결과를 갱신하기 위해 결과 변수의 초기값은 매우 큰 수로 설정
visited = [0] * N   # 방문한 도시인지 확인하기 위한 리스트

for i in range(N):  # 각 도시에서 시작하는 경우들을 모두 고려한다.
    dfs(i,i,0)
print(result)




# ------------------> 브루트포스 사용한 방법인데 Python3에서는 시간초과, pypy3에서는 틀림
# import sys

# # 입력
# N = int(sys.stdin.readline())
# cost = [0] * N
# for i in range(N):
#     cost[i] = list(map(int, sys.stdin.readline().split()))

# stk = []
# check = [0] * N
# summary = 0
# result = sys.maxsize

# # 탐색 함수
# def dfs():
#     global summary
#     global result
#     if len(stk) == N:   # 순열이 만들어지면
#         summary = 0
#         for j in range(0,len(stk)-1):   # 해당 순열 경로에서의 비용 합을 구함
#             if summary > result:    # summary가 result보다 커지면 바로 끊어준다.
#                 break

#             if j == len(stk)-2: # 마지막 방문 도시일때는
#                 summary += cost[stk[j]][stk[j+1]]
#                 summary += cost[stk[-1]][stk[0]]    # 자신한테 돌아오는 경로의 비용도 더해줌
#             else:
#                 summary += cost[stk[j]][stk[j+1]]
#         result = min(result, summary)   # 결과값 갱신
#         return

#     for i in range(N):  # 순열 만들기
#         if check[i] == 1 or (len(stk) > 1 and cost[stk[-1]][i] == 0):
#             continue
#         stk.append(i)
#         check[i] = 1
#         dfs()
#         stk.pop()
#         check[i] = 0

# dfs()
# print(result)