def move_hanoi(m, n, N):
    global count, lst

    if N == 1:
        lst.append([m+1, n+1])
        count += 1
    else:
        move_hanoi(m, 3-m-n, N-1)
        lst.append([m+1, n+1])
        count += 1
        move_hanoi(3-m-n, n, N-1)

if __name__ == "__main__":
    N = int(input())    
    count, lst = 0, []
    move_hanoi(0, 2, N)

    print(count)
    for l in lst:
        print(l[0], l[1])