import copy

def oper(ival, jval):
    lst = [ival + jval, ival * jval]
    if ival >= jval:
        lst.append(ival - jval)
    if jval != 0:
        lst.append(ival // jval)
    return lst

def solution(N, number):
    dp = [0, [N]]
    chkset = set([N])
    for i in range(1,9):
        tmpset = copy.deepcopy(chkset)
        for j in range(1,i+1):
            k = i+1-j
            for dpj in dp[j]:
                for dpk in dp[k]:
                    tmpset.update(oper(dpj, dpk))
        if number in tmpset:
            return i
        chkset.update(tmpset)
        
    return -1

# print(solution(1,1))
print(solution(5,12))

"""
# 1번째 시도: 이전 단계의 숫자들에만 한번 연산 시도

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
"""