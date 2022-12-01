answer = [0, 0]
posmap = [ (0,0), (0,1), (1,0), (1,1) ]
orig_map = []

def chk_all_data(map):
    global answer
    tmpval = map[0][0]
    for row in map:
        for crntposval in row:
            if crntposval != tmpval:
                return False
    return True

def main_recur(i, j, main_idx):
    global answer

    tmpmap = []
    for tmpi in range(i, i + main_idx):
        tmprow = []
        for tmpj in range(j, j + main_idx):
            tmprow.append(orig_map[tmpi][tmpj])
        tmpmap.append(tmprow)

    if chk_all_data(tmpmap):
        answer[tmpmap[0][0]] += 1
    else:
        main_idx = main_idx//2
        for quadpos in posmap:
            nxt_i = i + main_idx * quadpos[0]
            nxt_j = j + main_idx * quadpos[1]
            main_recur(nxt_i, nxt_j, main_idx)        

if __name__ == "__main__":    
    main_idx = int(input())

    for _ in range(main_idx):
        tmp_row = list(map(int, input().split()))
        orig_map.append(tmp_row)

    main_recur(0, 0, main_idx)
    
    print(answer[0])
    print(answer[1])


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