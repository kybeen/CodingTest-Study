# 암호 만들기

import sys

def dfs():
    global ja, mo
    if len(password) == L:  # 암호의 길이가 L이 되고
        if mo >= 1 and ja >= 2: # 모음이 1개 이상, 자음이 2개 이상 있으면 암호 출력
            print(*password,sep='') # 가능한 각 password들을 공백 없이 출력(이거 안해서 자꾸 틀렸음)
            return
            
    for i in range(0,C):
        # 이미 password에 들어있거나 사전순으로 앞에 오는 알파벳인 경우 continue
        if words[i] in password or (len(password) >= 1 and words[i] < password[-1]):
            continue
        # 암호문자 추가할때
        if words[i] == 'a' or words[i] == 'i' or words[i] == 'o' or words[i] == 'u' or words[i] == 'e': # 모음일 경우
            mo += 1
            password.append(words[i])
        else:   # 자음일 경우
            ja += 1
            password.append(words[i])

        dfs()   # 재귀호출

        # 암호문자 pop할때
        if password[-1] == 'a' or password[-1] == 'i' or password[-1] == 'o' or password[-1] == 'u' or password[-1] == 'e': # 모음일 경우
            mo -= 1
            password.pop()
        else:   # 자음일 경우
            ja -= 1
            password.pop()

L, C = map(int, sys.stdin.readline().split())
words = list(sys.stdin.readline().split())
password = []
ja, mo = 0, 0   # 자음모음 개수 카운트하기 위한 변수

words.sort()    # 먼저 입력받은 알파벳들을 사전순으로 정렬

dfs()   # dfs함수 실행