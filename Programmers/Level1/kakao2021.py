# 프로그래머스 2021 카카오 블라인드 채용
# LEVEL 1
# [ 신규 아이디 추천 ]
def solution(new_id):
    answer = ''
    # step 1 대문자 -> 소문자로
    new_id = new_id.lower()
    # step 2 소문자 숫자 - _ .만 남기기
    for letter in new_id:
        if letter.isalpha() or letter.isdigit():
            answer += letter
        elif letter == '-' or letter == '_' or letter == '.':
            answer += letter
    # step 3 마침표 2개 이상 연속된거 하나로
    temp = ''
    for i in range(len(answer)):
        isComma = False
        if i != 0 and answer[i] == '.' and answer[i-1] != '.':
            isComma = True
            
        temp += answer[i]
    # step 4 마침표가 처음이나 끝에 있으면 제거
    # step 5 빈 문자열이라면 new_id에 "a" 대입
    # step 6 길이가 16자 이상이라면 new_id의 첫 15개 문자만 남기기
    # step 7 길이가 2자 이하라면 new_id의 마지막 문자를 길이가 3이 될 때까지 붙이기
        
    return answer


result = solution("...!@BaT#*..y.abcdefghijklm")
print(result)