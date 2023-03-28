from collections import Counter

def solution(k, tangerine):
    counted = Counter(tangerine)
    most_srtd = sorted(counted.values(), reverse=True)#, key=lambda x: x[1])
    
    crnt_cnt, answer = 0, 0
    for cnt in most_srtd:
        crnt_cnt += cnt
        answer += 1
        if crnt_cnt >= k:
            return answer


if __name__ == "__main__":
    k = 6
    tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
    print(solution(k, tangerine))