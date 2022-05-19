def solution(msg):
    answer = []
    dic = {chr(i + ord('A')): i+1 for i in range(26)}
    leng = 27
    tmpstr = ""
    
    for chrc in msg:
        tmpstr += chrc
        if tmpstr not in dic.keys():
            answer.append(dic[tmpstr[:-1]])
            dic[tmpstr] = leng
            leng += 1
            tmpstr = tmpstr[-1]
    answer.append(dic[tmpstr])

    return answer

print(solution('KAKAO'))