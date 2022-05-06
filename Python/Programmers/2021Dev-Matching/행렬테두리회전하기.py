# 다른 사람 풀이 반영
# 테두리를 큐에 담을 때 아예 최소값 구하기
from collections import deque

def rotate(arr, x1, y1, x2, y2):
    q = deque([])
    for j in range(y1, y2):
        q.append(arr[x1][j])
    for i in range(x1, x2):
        q.append(arr[i][y2])
    for j in range(y2, y1, -1):
        q.append(arr[x2][j])
    for i in range(x2, x1, -1):
        q.append(arr[i][y1])

    q.appendleft(q.pop())
    tmpans = min(q)
    for j in range(y1, y2):
        arr[x1][j] = q.popleft()
    for i in range(x1, x2):
        arr[i][y2] = q.popleft()
    for j in range(y2, y1, -1):
        arr[x2][j] = q.popleft()
    for i in range(x2, x1, -1):
        arr[i][y1] = q.popleft()

    return tmpans

def solution(rows, columns, queries):
    answer = []

    arr = [[0]*(columns+1) for _ in range(rows+1)]
    tmpnum = 1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            arr[i][j] = tmpnum
            tmpnum += 1
            
    for query in queries:
        answer.append(rotate(arr, *query))

    return answer

    
rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows, columns, queries)

"""
# 내 1차 풀이
def rotate(arr, x1, y1, x2, y2):
    q = deque([])
    for j in range(y1, y2):
        q.append(arr[x1][j])
    for i in range(x1, x2):
        q.append(arr[i][y2])
    for j in range(y2, y1, -1):
        q.append(arr[x2][j])
    for i in range(x2, x1, -1):
        q.append(arr[i][y1])

    q.appendleft(q.pop())
    for j in range(y1, y2):
        arr[x1][j] = q.popleft()
    for i in range(x1, x2):
        arr[i][y2] = q.popleft()
    for j in range(y2, y1, -1):
        arr[x2][j] = q.popleft()
    for i in range(x2, x1, -1):
        arr[i][y1] = q.popleft()
        
def mininedge(arr, x1, y1, x2, y2):
    tmplst = []
    for j in range(y1, y2):
        tmplst.append(arr[x1][j])
    for i in range(x1, x2):
        tmplst.append(arr[i][y2])
    for j in range(y2, y1, -1):
        tmplst.append(arr[x2][j])
    for i in range(x2, x1, -1):
        tmplst.append(arr[i][y1])

    return min(tmplst)

def solution(rows, columns, queries):
    answer = []

    arr = [[0]*(columns+1) for _ in range(rows+1)]
    tmpnum = 1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            arr[i][j] = tmpnum
            tmpnum += 1
            
    for query in queries:
        rotate(arr, *query)
        answer.append(mininedge(arr, *query))

    return answer
"""