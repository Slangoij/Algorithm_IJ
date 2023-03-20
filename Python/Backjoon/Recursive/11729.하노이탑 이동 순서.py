count = 0

def mv1()

def move_hanoi(m, N):
    if m == 1:
        print()
        count += 1
        
    move_hanoi(m-1, N)
    print(m)
    move_hanoi(m-1, N)

if __name__ == "__main__":
    N = int(input())
    move_hanoi(N)