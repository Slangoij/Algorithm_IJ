def solution(s):
    answer = 1
    tmp_cnt = [0, 0]
    tmp_char = s[0]

    for cha in s:
        if tmp_cnt != [0,0] and tmp_cnt[0] == tmp_cnt[1]:
            if cha != tmp_char:
                tmp_char = cha
            tmp_cnt = [0, 1]
            answer += 1
        else:
            tmp_cnt[int(cha == tmp_char)] += 1

    return answer

if __name__ == "__main__":

    s = "aaabbaccccabba"
    
    print(solution(s))

"""
banana
abracadabra
aaabbaccccabba
"""