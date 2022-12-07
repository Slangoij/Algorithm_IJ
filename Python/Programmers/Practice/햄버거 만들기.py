"""
순서가 중요하므로 스택 이용만 하면 풀리는 문제
"""

def make_ham(que):
    if que[0] < 2:
        return False
    for i in que[1:]:
        if i < 1:
            return False
    return True

def solution(ingredient):
    answer = 0
    que_set = [0,0,0,0]

    for i in ingredient:
        que_set[i] += 1
        if make_ham(que_set[1:]):
            answer += 1
            que_set = [0,0,0,0]

    return answer

if __name__ == "__main__":

    ing = [1, 3, 2, 1, 2, 1, 3, 1, 2]

    print(solution(ing))

"""
[2, 1, 1, 2, 3, 1, 2, 3, 1]
[1, 3, 2, 1, 2, 1, 3, 1, 2]
"""