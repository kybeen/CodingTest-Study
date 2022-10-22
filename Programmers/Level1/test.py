# def solution(n, lost, reserve):
#     answer = n - len(lost)
#     for i in reserve:
#         if i in lost:
#             answer += 1
#             lost.remove(i)
#             reserve.remove(i)
#         print(i, answer, lost, reserve)
#     for i in reserve:
#         if i > 1 and i-1 in lost:
#             answer += 1
#             lost.remove(i-1)
#             print(i, answer, lost, reserve)
#         elif i < n and i+1 in lost:
#             answer += 1
#             lost.remove(i+1)
#             print(i, answer, lost, reserve)
#     return answer

# result = solution(10, [2,5,7,9], [1,6,9])
# print(result)



def solution(participant, completion):
    answer = ''
    participant_temp = participant
    for i in range(len(participant_temp)):
        if participant_temp[i] in completion:
            participant.remove(participant_temp[i])
            completion.remove(participant_temp[i])
    
    for i in participant:
        answer += i
    return answer

result = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
print(result)