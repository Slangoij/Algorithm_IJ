def ismatchquerinf(inf, quer):
    for idx in range(4):
        if quer[idx] != '-':
            if inf[idx] != quer[idx]:
                return False
    if int(inf[-1]) < int(quer[-1]):
        return False
    return True

def chkquer(info, quer):
    cnt = 0
    for inf in info:
        querlst = quer.split()
        newquer = [querlst[i] for i in [0,2,4,6,7]]
        newinf = inf.split()
        if ismatchquerinf(newinf, newquer):
            cnt += 1
    return cnt

def solution(info, query):
    answer = []
    for quer in query:
        answer.append(chkquer(info, quer))
            
    return answer

info = \
    ["java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"]
query = \
    ["java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"]
query = \
["- and backend and senior and - 150"]
print(solution(info, query))