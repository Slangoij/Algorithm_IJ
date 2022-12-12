"""
순서가 중요하므로 스택 이용만 하면 풀리는 문제
"""
from collections import deque

recipe = [1,2,3,1]
elstack = []

def solution(ingredient):
    answer, i = 0, 0

    for ing in ingredient:
        if ing == recipe[i]:
            i += 1
            if :
                pass
        else:
            elstack.append(ing)

    return answer

if __name__ == "__main__":

    ing = [2, 1, 1, 2, 3, 1, 2, 3, 1]

    print(solution(ing))

"""
[2, 1, 1, 2, 3, 1, 2, 3, 1]
[1, 3, 2, 1, 2, 1, 3, 1, 2]
"""