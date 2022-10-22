# 프로그래머스 DFS/BFS - 타겟 넘버
def solution(numbers, target):
    visited = []
    answer1 = DFS(numbers, target, 0, visited, 1)
    visited = []
    answer2 = DFS(numbers, target, 0, visited, -1)
    answer = answer1 + answer2
    
    return answer

def DFS(numbers, target, start, visited, case):
    answer = 0
    visited.append(numbers[start]*case)
    if len(numbers) == start+1:
        print(visited)
        if sum(visited) == target:
            return 1
        else:
            return 0
    else:
        answer += DFS(numbers, target, start+1, visited, case)
        visited.pop()
        numbers[start+1] *= -1
        answer += DFS(numbers, target, start+1, visited, case)
        visited.pop()
        return answer
    

print(solution([4,1,2,1], 4))