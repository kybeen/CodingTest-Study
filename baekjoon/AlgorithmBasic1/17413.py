#단어 뒤집기2

import sys

str = list(sys.stdin.readline().strip())
i = 0
index = 0
temp = []

while i < len(str):
    if str[i] == "<":
        while str[i] != ">":
            i += 1
        i += 1
    elif str[i].isalnum() == True:
        index = i
        while i < len(str) and str[i].isalnum() == True:
            i += 1
        temp = str[index:i]
        temp.reverse()
        str[index:i] = temp
    else:
        i += 1

print(''.join(str))