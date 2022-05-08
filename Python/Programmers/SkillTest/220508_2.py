# 두번째 풀이: 2차원 배열에 그리지 말고 좌표정보만 갖고 있자.
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
    # q_blocks = deque([])
    tmpblock = block
    for _ in range(4):
        tmpblock = list(reversed(list(zip(*tmpblock))))
        if tmpblock in blocks:
            break
        blocks.append(tmpblock)
        # for i in range(len(tmpblock)):
        #     for j in range(len(tmpblock[0])):
        #         if tmpblock[i][j]:
        #             q_blocks.append([i,j])

    # return q_blocks
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
    bl_hgt = len(block)
    bl_wdt = len(block[0])
    q_block = convert_arr_to_que(block)
    # 퍼즐움직이기
    for x_move in range(leng-bl_hgt+1):
        for y_move in range(leng-bl_wdt+1):
            # 퍼즐 모든 조각 맞는지 확인(주변까지)
            # 아래 인풋은 2차원 배열, 중간은 deque로 계산
            if chkPzAround(q_block, x_move, y_move):
                putPz(q_block, x_move, y_move)
                return True
    return False

    #         isfit = True
    #         for i in range(dx):
    #             for j in range(dy):
    #                 if block[i][j] + gameboard[i+x][j+y] != 1:
    #                     isfit = False
    #                 for ddx, ddy in dirs:
    #                     if i+ddx in range(dx) and j+ddy in range(dy)\
    #                         and i+x+ddx in range(len(gameboard)) and j+y+ddy in range(len(gameboard))\
    #                             and block[i+ddx][j+ddy] + gameboard[i+x+ddx][j+y+ddy] != 1:
    #                         isfit = False
    #         # 모든 조각 다 맞다면 퍼즐 카운팅
    #         if isfit:
    #             return True

    # return False

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

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
solution(game_board, table)
print(solution(game_board, table))



# # 첫번째 풀이: 완전 맵을 그려 구현
# # 문제 이해도 잘못했다. 퍼즐과 빈곳이 정확히 일치해야만 넣을 수 있는 것을 몰랐다.
# from collections import deque
# from copy import deepcopy

# dirs = [[0,1],[0,-1],[1,0],[-1,0]]
# gameboard = []
# glbanswer = 0

# def dfs(gameboard, blocks):
#     global glbanswer
#     tmpboard = deepcopy(gameboard)
#     nowblock = blocks.popleft()
#     dx = len(nowblock)
#     dy = len(nowblock[0])
#     for nowblock
#     for x in range(len(tmpboard)-dx+1):
#         for y in range(len(tmpboard)-dy+1):
#             for i in range(len(tmpboard)):
#                 for j in range(len(tmpboard)):
#                     if tmpboard[i+dx][j+dy] + nowblock[i][j] != 1:
#                         return
            
#             dfs(gameboard, )
#     dfs(gameboard, blocks)

# def rotatedblocks(block):
#     blocks = []
#     tmpblock = block
#     for i in range(4):
#         tmpblock = reversed(list(zip(*tmpblock)))
#         if tmpblock in blocks:
#             break
#         blocks.append(tmpblock)
#     return blocks

# def getblock(table, vstd, i, j):
#     q = deque([(i,j)])
#     quetochk = deque((i,j))
#     minx, maxx = i, i
#     miny, maxy = j, j
#     while q:
#         nx,ny = q.popleft()
#         for dx, dy in dirs:
#             cx, cy = nx+dx, ny+dy
#             if cx in range(len(table)) and cy in range(len(table))\
#                 and not vstd[cx][cy] and table[cx][cy] == 1:
#                 q.append((cx,cy))
#                 quetochk.append((cx,cy))
#                 vstd[cx][cy] = True
#                 minx, miny = min(cx, minx), min(cy, miny)
#                 maxx, maxy = max(cx, maxx), max(cy, maxy)

#     arr = [[0]*(maxy-miny+1) for _ in range(maxx-maxy+1)]
#     while quetochk:
#         x, y = quetochk.pop()
#         arr[x][y] = 1

#     return arr

# def solution(game_board, table):
#     global glbanswer
#     vstd = [[False]*len(table) for _ in range(len(table))]
#     blocks = deque([])

#     leng = len(game_board)
#     for i in range(leng):
#         for j in range(leng):
#             if not vstd[i][j]:
#                 blocks.append(getblock(table, vstd, i, j))

#     dfs(game_board, blocks)


#     return answer