from collections import deque
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def chkdistall(arr):
    p_coords = []
    for i in range(5):
        for j in range(5):
            if arr[i][j] == "P":
                p_coords.append([i,j])
    for x, y in p_coords:
        if not bfs(arr, x, y):
            return False
    return True

def bfs(arr, x, y):
    vstd = [[False]*5 for _ in range(5)]
    q = deque([(x, y, 0)])
    vstd[x][y] = True
    cx, cy = x, y
    while q:
        cx, cy, dist = q.popleft()
        for dx, dy in dirs:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<5 and 0<=ny<5 and arr[nx][ny] and not vstd[nx][ny]:
                vstd[nx][ny] = True
                if arr[nx][ny] == "P":
                    if dist < 2:
                        return False
                elif arr[nx][ny] == "O":
                    q.append((nx, ny, dist+1))
    return True

def solution(places):
    answer = []

    for place in places:
        if chkdistall(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer

places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
      ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
       ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# solution(places)
for i in places:
    print(chkdistall(i))