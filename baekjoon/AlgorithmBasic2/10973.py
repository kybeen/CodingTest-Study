# 이전 순열
#==> [10972 다음 순열] 문제에서 괄호만 몇개 바꾸고 정렬을 내림차순으로 하면 됨

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

flag = 0
for i in range(N-1, 0, -1):
    if arr[i-1] > arr[i]:   # 큰 수 나타나면
        for j in range(N-1, 0, -1):
            if arr[j] < arr[i-1]:
                arr[j], arr[i-1] = arr[i-1], arr[j] # 자기보다 작은 수 중 끝에서 가장 가까운 수와 바꾼다.
                flag = 1
                result = arr[:i] + sorted(arr[i:],reverse=True)  # 비뀐 자리 기준 오른쪽 수들은 내림차순 정렬해서 출력
                print(*result)  # 리스트의 원소만 출력([]랑 , 출력 안함)
                break
    if flag == 1:    # 답을 찾았을 경우 이중for문 탈출
        break
if flag == 0:
    print('-1')