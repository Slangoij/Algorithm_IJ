from math import factorial

def solution(N, M):
    return int(factorial(M) / (factorial(N) * factorial(M - N)))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(solution(N, M))
