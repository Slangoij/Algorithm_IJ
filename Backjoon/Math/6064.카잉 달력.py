import sys
input = sys.stdin.readline
from math import gcd

T = int(input())
answer = []
for _ in range(T):
    M, N, x, y = map(int, input().split())

    if M == N:
        if x == y:
            answer.append(x)
        else:
            answer.append(-1)
        continue
    if M > N:
        M,N = N,M
        x,y = y,x

    lcm = M*N//gcd(M,N)
    tmpans = -1
    for i in range(x, lcm+1, M):
        if (i-1)%N == y-1:
            tmpans = i
            break
    answer.append(tmpans)

for ans in answer:
    print(ans)

"""

3
10 12 3 9
10 12 7 2
13 11 5 6

1
10 12 3 9

1
40000 39999 39999 39998

15
40000 39999 39999 39998
40000 39999 40000 39999
40000 40000 40000 39999
40000 39998 40000 39997
39999 2 39998 2
3 40000 3 39999
40000 3 40000 3
8 2 4 2
10 12 2 12
12 10 12 10
12 10 1 1
12 6 12 6
10 1 5 1
1 10 1 5
1 1 1 1

1
39999 2 39998 2

1
3 4 3 4

"""

# # 1번째 추론:
# # 각 숫자에 기준 M,N 을 더해가면서 같은 수가 나온다면 (M*N의 범위 안에서)
# # 그 같은 수가 마지막 해이다 결과는 맞겠지만 찾는 과정에서 숫자를 각각 더해가면서 비교하는 과정이
# # 비효율적인 듯
# X, Y = x, y
# while X != Y and X*Y < M*N:
#     if X>Y:
#         Y += ((X-Y)//N)*N
#     else:
#         X += ((Y-X)//M)*M
#     if X*Y > M*N:
#         answer.append(-1)
#     else:
#         answer.append(X)


# # 2번째 시도: 각각의 배수들을 더한 모든 집합을 구해서 교집합으로
# # 겹치는 부분 구했는데 메모리가 아쉽나? 답도 틀렸다
# xset = set([tmp for tmp in range(x,maxx-x+1, M)])
# yset = set([tmp for tmp in range(y,maxx-y+1, N)])
# if not xset.intersection(yset):
#     answer.append(-1)
#     continue

# tmpans = min(xset.intersection(yset))
# if tmpans <= maxx:
#     answer.append(tmpans)
# else:
#     answer.append(-1)

# # 3번째 시도
# # 연산량을 줄이기 위해 리스트로 확인하는 걸로 대체했지만 여전히 시간초과
# if M == N:
#     if x == y:
#         answer.append(x)
#     else:
#         answer.append(-1)
#     continue
# if M > N:
#     M,N = N,M
#     x,y = y,x
# tmpans, nowval = x,x
# gap = N - M
# tmplst = [False]*(N+1)
# while True:
#     if tmplst[nowval] or tmpans > M*N:
#         tmpans = -1
#         break
#     tmplst[nowval] = True
#     if nowval == y:
#         break

#     tmpans += M
#     nowval = (nowval-gap-1)%N + 1


# if tmpans > M*N or tmpans == -1:
#     answer.append(-1)
# else:
#     answer.append(tmpans)