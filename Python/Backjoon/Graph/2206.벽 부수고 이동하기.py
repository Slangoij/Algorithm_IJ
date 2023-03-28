from collections import deque

answer = -1
n,m = map(int, input().split())
vstd = [[False] * m for _ in range(n)]
mapp = []
for _ in range(n):
    mapp.append( list(input()) )

dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque([[0,0,1,False]])
vstd[0][0] = True
while q:
    (c_y, c_x, cnt, is_brk) = q.popleft()
    if c_x == m-1 and c_y == n-1:
        if answer == -1: answer = cnt
        else: answer = min(answer, cnt)
        continue
    
    for dir in range(4):
        n_x, n_y = c_x + dx[dir], c_y + dy[dir]
        if n_x in range(m) and n_y in range(n) and not vstd[n_y][n_x]:
            crnt_brkn = is_brk
            if mapp[n_y][n_x] == '0' or not is_brk:
                if mapp[n_y][n_x] == '1': crnt_brkn = True
                vstd[n_y][n_x] = True
                q.append([n_y, n_x, cnt+1, crnt_brkn])

print(answer)

"""
6 4
0100
1110
1000
0000
0111
0000

"""