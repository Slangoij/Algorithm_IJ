def solution(record):
    answer = []
    result = []
    userinfo = {}
    for msg in record:
        spltmsg = msg.split(" ")

        if spltmsg[0] == "Change":
            userinfo[spltmsg[1]] = spltmsg[2]
        else:
            if spltmsg[0] == "Enter":
                result.append([spltmsg[1], "님이 들어왔습니다."])
                userinfo[spltmsg[1]] = spltmsg[2]
            elif spltmsg[0] == "Leave":
                result.append([spltmsg[1], "님이 나갔습니다."])
        
    for msg in result:
        answer.append(userinfo[msg[0]] + msg[1])

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
for i in solution(record):
    print(i)