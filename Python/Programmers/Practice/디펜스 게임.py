def solution(n, k, enemy):
    nxt_n = n

    idx_chk = 0
    for idx in range(len(enemy)):
        if n >= enemy[idx]:
            n -= enemy[idx]
        else:
            idx_chk = min(idx, len(enemy))

    tmp_lst = sorted(enemy[:idx_chk + k])
    for idx in range(len(tmp_lst)):
        if nxt_n >= enemy[idx]:
            nxt_n -= enemy[idx]
        else:
            return min(idx + k, len(enemy))

    return len(enemy)

if __name__ == "__main__":
    n = 2
    k = 1
    enemy = [1,8,1]
    
    print(solution(n,k,enemy))