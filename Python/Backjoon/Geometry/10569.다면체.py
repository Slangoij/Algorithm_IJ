T = int(input())

def solution(V, E):
    return 2 - V + E

for i in range(T):
    V, E = map(int, input().split())
    print(solution(V, E))