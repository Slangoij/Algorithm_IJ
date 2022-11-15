main_idx = int(input())

answer = 0
posmap = [
    (0,0), (0,1), (1,0), (1,1)
]
orig_map = []

def chk_all_data(map):
    tmpval = map[0][0]
    for row in map:
        for data in row:
            if data != tmpval:
                return False
    return True

def get_crnt_map(map):
    pass

def main_recur(i, j):
    global answer, main_idx
    for quadpos in posmap:
        tmpmap = []
        crnt_pos_i = int(i + main_idx*quadpos[0])
        crnt_pos_j = int(j + main_idx*quadpos[1])
        for tmpi in range(crnt_pos_i, crnt_pos_i + main_idx):
            tmprow = []
            for tmpj in range(crnt_pos_j, crnt_pos_j + main_idx):
                tmprow.append(orig_map[tmpi][tmpj])
            tmpmap.append(tmprow)

        if chk_all_data(tmpmap):
            answer += 1
        else:
            main_idx = main_idx//2
            main_recur(crnt_pos_i, crnt_pos_j)

if __name__ == "__main__":
    for _ in range(main_idx):
        tmp_row = list(map(int, input().split()))
        orig_map.append(tmp_row)

    main_recur(0, 0)
    print(answer)


"""
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

"""