#스택 수열

n = int(input())
error = 0
count = 1
num_stack = []
result = []

for i in range(0,n):
    num = int(input())
    while count <= num:
        num_stack.append(count)
        count += 1
        result.append('+')

    if num_stack[-1] == num:
        num_stack.pop()
        result.append('-')
    else:
        error = 1

if error == 1:
    print("NO")
else:
    for i in result:
        print(i)