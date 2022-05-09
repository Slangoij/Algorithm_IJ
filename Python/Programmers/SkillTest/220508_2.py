# 두번째 풀이: 2차원 배열에 그리지 말고 좌표정보만 갖고 있자.
from collections import deque
import copy

dirs = [[0,1],[0,-1],[1,0],[-1,0]]

def convert_arr_to_que(block):
    q_blocks = deque([])
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j]:
                q_blocks.append([i,j])
    return sorted(list(q_blocks), key=lambda x: (x[0],x[1]))

def rotatedblockarr(block):
    q_blocks = []
    tmpblock = block
    for _ in range(4):
        q_blocks.append(tmpblock)
        tmpblock = list(reversed(list(zip(*tmpblock))))
        if tmpblock in q_blocks:
            break
    return q_blocks

def getblockarr(table, vstd, i, j):
    vstd[i][j] = True
    q = deque([(i,j)])
    minx, maxx = i, i
    miny, maxy = j, j
    quetochk = deque([(i,j)])
    while q:
        nx,ny = q.popleft()
        for dx, dy in dirs:
            cx, cy = nx+dx, ny+dy
            if cx in range(len(table)) and cy in range(len(table))\
                and not vstd[cx][cy] and table[cx][cy] == 1:
                q.append((cx,cy))
                quetochk.append((cx,cy))
                vstd[cx][cy] = True
                minx, miny = min(cx, minx), min(cy, miny)
                maxx, maxy = max(cx, maxx), max(cy, maxy)

    arr = [[0]*(maxy-miny+1) for _ in range(maxx-minx+1)]
    while quetochk:
        x, y = quetochk.pop()
        arr[x-minx][y-miny] = 1
    return arr

def getholeque(game_board, vstd, i, j):
    vstd[i][j] = True
    q = deque([(i,j)])
    minx, maxx = i, i
    miny, maxy = j, j
    quetochk = deque([(i,j)])
    while q:
        nx,ny = q.popleft()
        for dx, dy in dirs:
            cx, cy = nx+dx, ny+dy
            if cx in range(len(game_board)) and cy in range(len(game_board))\
                and not vstd[cx][cy] and game_board[cx][cy] == 0:
                q.append((cx,cy))
                quetochk.append((cx,cy))
                vstd[cx][cy] = True
                minx, miny = min(cx, minx), min(cy, miny)
                maxx, maxy = max(cx, maxx), max(cy, maxy)

    que = []
    for x, y in list(quetochk):
        que.append([x-minx,y-miny])
    return sorted(que, key=lambda x: (x[0],x[1]))
    
def match(hole, block):
    for rotblock in list(rotatedblockarr(block)):
        if hole == convert_arr_to_que(rotblock):
            return len(hole)
    return 0

def solution(game_board, table):
    global glb_game_board
    glb_game_board = copy.deepcopy(game_board)
    answer = 0
    holes, blocks = [], []

    table_vstd = [[False]*len(table) for _ in range(len(table))]
    table_leng = len(table)
    for i in range(table_leng):
        for j in range(table_leng):
            if not table_vstd[i][j] and table[i][j] == 1:
                blocks.append(getblockarr(table, table_vstd, i, j))

    board_vstd = [[False]*len(table) for _ in range(len(table))]
    board_leng = len(game_board)
    for i in range(board_leng):
        for j in range(board_leng):
            if not board_vstd[i][j] and game_board[i][j] == 0:
                holes.append(getholeque(game_board, board_vstd, i, j))

    for hole in holes:
        if blocks:
            for block in blocks:
                tmpret =  match(hole, block)
                if tmpret:
                    answer += tmpret
                    blocks.remove(block)
                    break

    return answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
# game_board = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
# table = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]
# solution(game_board, table)
print(solution(game_board, table))


"""
# 2차 풀이: 시간 초과
from collections import deque
import copy

dirs = [[0,1],[0,-1],[1,0],[-1,0]]
glb_game_board = []

def convert_arr_to_que(block):
    q_blocks = deque([])
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j]:
                q_blocks.append([i,j])
    return q_blocks

def chkPzAround(q_block, x_move, y_move):
    global glb_game_board
    leng = len(glb_game_board)
    maptochkblock = [[False]*leng for _ in range(leng)]
    tmp_block = copy.deepcopy(q_block)
    for x, y in list(q_block):
        maptochkblock[x+x_move][y+y_move] = True
    while tmp_block:
        x, y = tmp_block.popleft()
        x, y = x + x_move, y + y_move
        for dx, dy in dirs:
            cx, cy = x+dx, y+dy
            if cx in range(leng) and cy in range(leng):
                if maptochkblock[cx][cy]:
                    if glb_game_board[cx][cy] != 0:
                        return False
                else:
                    if glb_game_board[cx][cy] != 1:
                        return False
    return True

def putPz(q_block, x_move, y_move):
    global glb_game_board
    for x, y in list(q_block):
        glb_game_board[x+x_move][y+y_move] = 1

def rotatedblocks(block):
    blocks = []
    tmpblock = block
    for _ in range(4):
        tmpblock = list(reversed(list(zip(*tmpblock))))
        if tmpblock in blocks:
            break
        blocks.append(tmpblock)
    return blocks

def getblockarr(table, vstd, i, j):
    vstd[i][j] = True
    q = deque([(i,j)])
    quetochk = deque([(i,j)])
    minx, maxx = i, i
    miny, maxy = j, j
    while q:
        nx,ny = q.popleft()
        for dx, dy in dirs:
            cx, cy = nx+dx, ny+dy
            if cx in range(len(table)) and cy in range(len(table))\
                and not vstd[cx][cy] and table[cx][cy] == 1:
                q.append((cx,cy))
                quetochk.append((cx,cy))
                vstd[cx][cy] = True
                minx, miny = min(cx, minx), min(cy, miny)
                maxx, maxy = max(cx, maxx), max(cy, maxy)

    arr = [[0]*(maxy-miny+1) for _ in range(maxx-minx+1)]
    while quetochk:
        x, y = quetochk.pop()
        arr[x-minx][y-miny] = 1

    return arr
    
def chkblck(block):
    global glb_game_board
    leng = len(glb_game_board)
    x, y = list(zip(*list(block)))
    bl_hgt = max(x) - min(x)
    bl_wdt = max(y) - min(y)
    # 퍼즐움직이기
    for x_move in range(leng-bl_hgt):
        for y_move in range(leng-bl_wdt):
            # 퍼즐 모든 조각 맞는지 확인(주변까지)
            # 아래 인풋은 2차원 배열, 중간은 deque로 계산
            putPz(block, x_move, y_move) # 일단 넣어보고
            if not chkPzAround(block, x_move, y_move): # 안맞으면 빼고
                liftPz(block, x_move, y_move)
            else:  # 맞으면 넣은 그대로 계산
                return True

    return False

def solution(game_board, table):
    global glb_game_board
    glb_game_board = copy.deepcopy(game_board)
    answer = 0
    vstd = [[False]*len(table) for _ in range(len(table))]
    blocks = deque([])

    leng = len(table)
    for i in range(leng):
        for j in range(leng):
            if not vstd[i][j] and table[i][j]:
                blocks.append(getblockarr(table, vstd, i, j))

    while blocks:
        nowblock = blocks.popleft()
        nowblocks = rotatedblocks(nowblock)
        dx = len(nowblock)
        dy = len(nowblock[0])
        blocksize = 0
        for i in range(dx):
            for j in range(dy):
                if nowblock[i][j]:
                    blocksize += 1
        for block in nowblocks:
            if chkblck(block):
                answer += blocksize
                break

    return answer
"""

"""
# 첫번째 풀이: 완전 맵을 그려 구현
# 문제 이해도 잘못했다. 퍼즐과 빈곳이 정확히 일치해야만 넣을 수 있는 것을 몰랐다.
from collections import deque
from copy import deepcopy

dirs = [[0,1],[0,-1],[1,0],[-1,0]]
gameboard = []
glbanswer = 0

def dfs(gameboard, blocks):
    global glbanswer
    tmpboard = deepcopy(gameboard)
    nowblock = blocks.popleft()
    dx = len(nowblock)
    dy = len(nowblock[0])
    for nowblock
    for x in range(len(tmpboard)-dx+1):
        for y in range(len(tmpboard)-dy+1):
            for i in range(len(tmpboard)):
                for j in range(len(tmpboard)):
                    if tmpboard[i+dx][j+dy] + nowblock[i][j] != 1:
                        return
            
            dfs(gameboard, )
    dfs(gameboard, blocks)

def rotatedblocks(block):
    blocks = []
    tmpblock = block
    for i in range(4):
        tmpblock = reversed(list(zip(*tmpblock)))
        if tmpblock in blocks:
            break
        blocks.append(tmpblock)
    return blocks

def getblock(table, vstd, i, j):
    q = deque([(i,j)])
    quetochk = deque((i,j))
    minx, maxx = i, i
    miny, maxy = j, j
    while q:
        nx,ny = q.popleft()
        for dx, dy in dirs:
            cx, cy = nx+dx, ny+dy
            if cx in range(len(table)) and cy in range(len(table))\
                and not vstd[cx][cy] and table[cx][cy] == 1:
                q.append((cx,cy))
                quetochk.append((cx,cy))
                vstd[cx][cy] = True
                minx, miny = min(cx, minx), min(cy, miny)
                maxx, maxy = max(cx, maxx), max(cy, maxy)

    arr = [[0]*(maxy-miny+1) for _ in range(maxx-maxy+1)]
    while quetochk:
        x, y = quetochk.pop()
        arr[x][y] = 1

    return arr

def solution(game_board, table):
    global glbanswer
    vstd = [[False]*len(table) for _ in range(len(table))]
    blocks = deque([])

    leng = len(game_board)
    for i in range(leng):
        for j in range(leng):
            if not vstd[i][j]:
                blocks.append(getblock(table, vstd, i, j))

    dfs(game_board, blocks)


    return answer
"""