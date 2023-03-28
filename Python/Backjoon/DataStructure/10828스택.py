def solution():
    stck = []

    iter = int(input())
    for _ in range(iter):
        order = input()

        if len(order.split()) > 1:
            stck.append(order.split()[-1])
            print(order.split()[-1])
        else:
            stlen = len(stck)
            if order == "top":
                if stlen > 0: print(stck[stlen - 1])
                else: print(-1)
            elif order == "empty":
                if stlen > 0: print(0)
                else: print(1)
            elif order == "size":
                print(stlen)
            elif order == "pop":
                if stlen > 0: print(stck.pop())
                else: print(-1)

if __name__ == "__main__":
    solution()

stck = []

iter = int(input())
for _ in range(iter):
    order = input()

    if len(order.split()) > 1:
        stck.append(order.split()[-1])
        print(order.split()[-1])
    else:
        stlen = len(stck)
        if order == "top":
            if stlen > 0: print(stck[stlen - 1])
            else: print(-1)
        elif order == "empty":
            if stlen > 0: print(0)
            else: print(1)
        elif order == "size":
            print(stlen)
        elif order == "pop":
            if stlen > 0: print(stck.pop())
            else: print(-1)