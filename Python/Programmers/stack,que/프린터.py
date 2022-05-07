from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque([])
    for idx, prir in enumerate(priorities):
        q.append((idx, prir))
    
    while q:
        idx, prir = q.popleft()
        if q and prir < max(list(zip(*list(q)))[1]):
            q.append((idx, prir))
        else:
            answer += 1
            if idx == location:
                return answer
    
    return answer

priorities = [2,1,3,2]
location = 2
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
print(solution(priorities, location))