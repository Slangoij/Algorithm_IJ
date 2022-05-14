def solution(W, H, leng):
    if leng**2 <= W**2 + H**2:
        return "DA"
    else:
        return "NE"

N, W, H = map(int, input().split())

for _ in range(N):
    leng = int(input())
    print(solution(W, H, leng))