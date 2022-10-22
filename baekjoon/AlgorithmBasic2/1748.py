# 수 이어 쓰기
# ==> 자릿수 구간별로 자릿수 총 합의 규칙이 {9*10^(자릿수-1) * 자릿수}가 된다. 이 규칙을 사용해서 구해야 시간초과 안남

import sys

N = int(sys.stdin.readline())
count = 0
n_len = len(str(N))
if n_len == 1:
    count += N
else:
    for i in range(0,n_len-1):
        count += 9*(10**i) * (i+1)
    count += ((N - (10**(n_len - 1))) + 1) * n_len
print(count)
    



# -----------------------------> 구간별로 자릿수만큼 더하는 방식 ==> 얘도 시간초과
# import sys

# N = int(sys.stdin.readline())
# count = 0
# for i in range(1,N+1):
#     if 1 <= i < 10:
#         count += 1
#     if 10 <= i < 100:
#         count += 2
#     if 100 <= i < 1000:
#         count += 3
#     if 1000 <= i < 10000:
#         count += 4
#     if 10000 <= i < 100000:
#         count += 5
#     if 100000 <= i < 1000000:
#         count += 6
#     if 1000000 <= i < 10000000:
#         count += 7
#     if 10000000 <= i < 100000000:
#         count += 8
#     if i == 100000000:
#         count += 9
# print(count)


# --------------------------------> 문자열로 바꾼 뒤 문자열의 길이를 더하는 방식 => 시간초과
# import sys

# N = int(sys.stdin.readline())
# result = 0
# for i in range(1,N+1):
#     count = str(i)
#     result += len(count)
# print(result)