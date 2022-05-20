def solution(N, number):
    vstd = [False for _ in range(number*N+1)]
    dp = [0, [N]]
    vstd[N] = True
    for i in range(1,9):
        if number in dp[i]:
            return i
            
        tmpnxt = []
        ext = int(str(N)*(i+1))
        for j in dp[i]:
            pl = j+N
            mi = j-N
            mul = j*N
            div = j//N
            for k in [ext,pl,mi,mul,div]:
                if k in range(number*N+1) and not vstd[k]:
                    vstd[k] = True
                    tmpnxt.append(k)
        dp.append(tmpnxt)
    return -1

# print(solution(1,1))
print(solution(5,12))