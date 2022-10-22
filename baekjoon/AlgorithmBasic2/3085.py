# 사탕 게임 -----> 구글링함, 테이블 크기가 50보다 작기 때문에 코드의 시간복잡도가 O(N^4)이어도 ㄱㅊ

import sys

N = int(sys.stdin.readline())
board = [0] * N
for i in range(N):
    board[i] = list(sys.stdin.readline().rstrip())

# 같은색으로 연속된 사탕의 최대 개수 구하는 함수
def check(board):
    result = 0
    for i in range(N):
        row = 1
        col = 1
        for j in range(N-1):
            # 행 검사
            if board[i][j] == board[i][j+1]:
                row += 1
            else:
                result = max(result,row)
                row = 1
            # 열 검사
            if board[j][i] == board[j+1][i]:
                col += 1
            else:
                result = max(result,col)
                col = 1
            result = max(result,row,col)
    return result

result2 = 0
# 두 칸 바꾸는 경우별로 수행

for i in range(N):
    for j in range(N-1):
        # 가로로 다른 경우
        if board[i][j] != board[i][j+1]:    # 가로로 서로 다르면
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 바꾼다
            temp = check(board)    # 바뀐 보드에 대해서 사탕 최대개수 검사
            result2 = max(result2, temp)    # 더 큰 값이 나오면 결과값 갱신
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 바꾼 사탕 다시 원위치
        # 세로로 다른 경우도 똑같이 수행
        if board[j][i] != board[j+1][i]:
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            temp = check(board)
            result2 = max(result2, temp)
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(result2)