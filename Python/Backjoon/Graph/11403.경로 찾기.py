import heapq

mapp, answer = [], []
graph = {}

def dijkstra(stt):
    global answer
    q = []
    heapq.heappush(q, stt)
    while q :
        crnt_n = heapq.heappop(q)
        if  crnt_n != stt: continue
        for new_n in graph[crnt_n]:
            answer[stt][new_n] = 1
            heapq.heappush(q, new_n)

n = int(input())
for _ in range(n):
    mapp.append(list(map(int, input().split())))
    answer.append([0] * n)

for i in range(n):
    for j in range(n):
        if mapp[i][j]:
            if i in graph:
                graph[i] += j
            else:
                graph[i] = [j]

for i in range(n):
    dijkstra(i)

for i in range(n):
    print(' '.join(list(map(str, answer[i]))))