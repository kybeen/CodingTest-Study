# 연속합2 ------> 시간초과
# ==> dp[i][0] 원소 제거 안한 경우
# ==> dp[i][1] 제거된 원소가 있는 경우

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0,0] for i in range(n)]
dp[0][0] = arr[0]
if n == 1:  # n이 1이면 원소 하나를 무조건 선택해야 하므로 비로 dp[0][0]을 출력한다.
    print(dp[0][0])
elif n > 1:
    result = -(sys.maxsize) # max연산을 하기 위해 result의 초기값은 가장 작은 음의 정수로 한다.
    for i in range(1,n):
        # 원소를 제거하지 않는 경우는       (이전까지의 연속합 + i번째 원소) <==> (i번째 원소)      비교
        dp[i][0] = max(dp[i-1][0]+arr[i], arr[i])
        # 제거된 원소가 있는 경우는         자기를 제거할 때 <==> 이전에 제거된 원소가 있는 경우    비교
        dp[i][1] = max(dp[i-1][0], dp[i-1][1] + arr[i])
        result = max(result, dp[i][0], dp[i][1])    # 더 큰 연속합을 결과에 저장
    print(result)

#----------------------------------> 답은 나오는데 시간초과(알고리즘은 맞는듯)
# import sys

# def func(lst):
#     dp_table = [0] * len(lst)
#     dp_table[0] = lst[0]
#     for i in range(1,len(lst)):
#         dp_table[i] = lst[i]
#         dp_table[i]  = max(dp_table[i], dp_table[i-1]+lst[i])
#     return max(dp_table)

# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# result = func(arr)  # 수 제거 안했을 경우 최대값

# # 수 제거 했을 경우의 연속합 구하기(음수 원소만 제거한다) ==> 연산횟수가 너무 많아짐
# for i in arr:
#     if i < 0:
#         arr2 = arr[:arr.index(i)] + arr[arr.index(i)+1:]
#         result2 = func(arr2)
#         result = max(result, result2)
# print(result)