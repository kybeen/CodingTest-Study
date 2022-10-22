# 숫자 카드 게임
# N x M 형태로 숫자가 적힌 카드들 놓임
# 각 행에서 가장 작은 수들 중 가장 큰 수 고르는 문제 같은데 문제 이해가 잘 안됨;; 너무 쉽게 풀었는데
import sys

N, M = map(int, sys.stdin.readline().split())
cards = []
minimums = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    cards.append(temp)

for row in cards:
    minimums.append(min(row))

minimums.sort()
print(minimums[-1])