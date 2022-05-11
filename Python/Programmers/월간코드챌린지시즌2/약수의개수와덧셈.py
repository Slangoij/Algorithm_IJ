def get_prime_arr(n):
    arr = [True] * (n+1)
    arr[0], arr[1] = False, False

    for i in range(2, n+1):
        if arr[i]:
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j += 1
                
    tmpans = []
    for i in range(2, n+1):
        if arr[i]:
            tmpans.append(i)

    return tmpans

def solution(left, right):
    answer = 0

    isodd = [True for _ in range(right+1)]
    priarr = get_prime_arr(right)
    for prime in priarr:
        for i in range(left, right+1):
            tmpnum, multi = i, 0
            while tmpnum >= prime and tmpnum % prime == 0:
                tmpnum = tmpnum // prime
                multi += 1
            if multi and multi % 2 != 0:
                isodd[i] = False

    for i in range(left, right+1):
        if isodd[i]:
            answer -= i
        else:
            answer += i

    return answer

left, right = 13, 17
print(solution(left, right))