
"""
# 3차 시도: 힙에 넣고 빼는 데도 시간이 걸리는것같다.
# 이전까지는 테스트케이스 2까지 맞다가 그래도 여기선 3까지 맞춤
import heapq
import math

def lcm_each(a, b):
    return a * b // math.gcd(a, b)

def lcm(lst):
    if len(lst) == 1:
        return lst[0]
    ret = 1
    for i in range(len(lst)):
        ret = lcm_each(ret, lst[i])
    return ret

def solution(n, times):
    times.sort()
    line = [(time, time) for time in times]
    heapq.heapify(line)
    tmplcm = lcm(list(set(times)))
    timelst = []
    for _ in range(n):
        fintime, tact = heapq.heappop(line)
        if fintime > tmplcm:
            break
        timelst.append(fintime)
        heapq.heappush(line, (fintime+tact, tact))
    idx = n-1
    return timelst[idx%len(timelst)]\
        + timelst[-1] * (idx//len(timelst))
"""

n = 1000000000
times = [1000000000-i for i in range(100000)]
print(solution(n, times))

"""
# 2차 시도: 무조건 시간이 적은 대로 사람을 넣은 듯 
import heapq
import math

def lcm_each(a, b):
    return (int)(a * b / math.gcd(a, b))

def lcm(lst):
    if len(lst) == 1:
        return lst[0]
    ret = 1
    for i in range(len(lst)):
        ret = lcm_each(ret, lst[i])
    return ret

def solution(n, times):
    peoplecnt, fintime = 0, 0
    times.sort()
    line = [(time, time) for time in times]
    heapq.heapify(line)
    tmplcm = lcm(list(set(times)))

    tmplst = []
    while peoplecnt < n and fintime <= tmplcm:
        fintime, tact = heapq.heappop(line)
        heapq.heappush(line, (fintime + tact, tact))
        if fintime > tmplcm:
            break
        tmplst.append(fintime)
        peoplecnt += 1


    # return fintime, tmplst
    tmpidx = n-1
    if tmpidx < peoplecnt < n:
        return tmplst[tmpidx]
    return (tmpidx//peoplecnt)*tmplst[-1] + tmplst[tmpidx%peoplecnt]
"""

"""
# 1차 시도 :
# 사람이 전체 심사라인 이하면 무조건 하나씩 배정할거라고 착각.
# 사람이 무한정 많아지더라도 무조건 힙으로 계산. 힙은 logN의 복잡도기때문에 
# 2차적으로 더 줄이는 노력이 필요했음.

def solution(n, times):
    times.sort()
    leng = len(times)
    line = []
    if n <= leng:
        return times[n-1]
    line = [(time, time) for time in times]
    for _ in range(n-leng):
        fintime, tact = heapq.heappop(line)
        heapq.heappush(line, (fintime+tact, tact))

    return sum(line[0])
"""