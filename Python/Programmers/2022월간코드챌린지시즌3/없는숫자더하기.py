def solution(numbers):
    answer = 0
    dict = {i:True for i in range(10)}
    for i in numbers:
        dict[i] = False
    for i in range(10):
        if dict[i]:
            answer += i

    return answer