from sys import stdin

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(stdin.readline()))
new_lst = list(map(str, sorted(lst)))
print("\n".join(new_lst))