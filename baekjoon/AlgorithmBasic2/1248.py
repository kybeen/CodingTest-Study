# 맞춰봐 ==> 어렵고 복잡했는데 풀었음ㅎㅎ Python3은 시간초과, PyPy3로 하면 맞음

import sys

def check():
    if len(A) >= 1: # 현재 A의 길이가 1 이상이면 바로 S테이블과 값의 합이 일치하는지 검사하고 만족하지 않을 경우 리턴하여 검사 시간을 줄인다.
        start = 0
        for m in range(0,len(A)):
            summary = 0
            for n in range(start,len(A)):
                summary += A[n]
                if S[m][n] == '0' and summary != 0:
                    return
                elif S[m][n] == '+' and summary <= 0:
                    return
                elif S[m][n] == '-' and summary >= 0:
                    return
            start += 1
    # A의 길이가 N까지 됐다는 것은 조건을 만족하는 수열이 만들어졌다는 것이므로 출력하고 프로그램을 종료한다.
    if len(A) == N:
        print(*A)
        sys.exit()
    
    for i in range(21):
        A.append(num[i])
        check()
        A.pop()

N = int(sys.stdin.readline())
str = list(sys.stdin.readline())
num = [i for i in range(-10,11)]    # 적을 수 있는 숫자들 (-10 ~ 10)
A = []  # 결과 수열
S = [[0]*N for i in range(N)]   # S테이블
str_idx = 0 
# 입력받은 str을 바탕으로 S테이블을 먼저 만들어준다.
for i in range(N):
    for j in range(i,N):
        S[i][j] = str[str_idx]
        str_idx += 1

# 재귀함수 실행
check()