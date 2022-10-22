# 다음 순열 ==> 구글링함.
# ==> 뒤에서부터 검사하다가 작은 수가 나타나면 자리 바꿈. 비뀐 기준으로 오른쪽에 있는 숫자들은 오름차순 정렬 해주면 된다.

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

flag = 0
for i in range(N-1, 0, -1):
    if arr[i-1] < arr[i]:   # 작은 수 나타나면
        for j in range(N-1, 0, -1):
            if arr[j] > arr[i-1]:
                arr[j], arr[i-1] = arr[i-1], arr[j] # 자기보다 큰 수 중 끝에서 가장 가까운 수와 바꾼다.
                flag = 1
                result = arr[:i] + sorted(arr[i:])  # 비뀐 자리 기준 오른쪽 수들은 정렬해서 출력
                print(*result)
                break
    if flag == 1:    # 답을 찾았을 경우 이중for문 탈출
        break
if flag == 0:
    print('-1')



#---------------------------------> 런타임에러(RecursionError) 뜸, 재귀횟수가 많아져서 그런거같음
# import sys

# # 15663 코드를 활용하여 사전순으로 정렬되도록 스택에 숫자를 추가한 후 result로 순열들을 넣어준다.
# def dfs():
#     if len(stk) == N:
#         result.append(stk[:])   # 순열을 result에 추가
#         return
#     for i in range(1,N+1):
#         if i in stk:
#             continue
#         stk.append(i)
#         dfs()
#         stk.pop()

# N = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# stk = []
# result = []

# dfs()
# for i in range(0,len(result)-1):
#     if result[i] == arr:    # result에 들어있는 순열 원소 중 입력받은 arr과 똑같은 순열을 발견하면 다음 순열을 출력
#         print(' '.join(map(str,result[i+1])))
#         break
# if result[-1] == arr:   # result의 마지막 원소와 입력받은 arr이 같을 경우 -1을 출력
#     print('-1')