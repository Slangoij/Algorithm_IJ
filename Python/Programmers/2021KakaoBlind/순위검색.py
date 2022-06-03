
# 3차 시도: 결국 답안 참조. 문자열은 모두 unique한 특성이 있으므로 여러 조합으로
# 직접 dictionary의 키로 활용가능.
def solution(info, query):
    answer = []

    infobase = dict()
    for lang in ['cpp', 'java', 'python', '-']:
        for job in ['backend', 'frontend', '-']:
            for care in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    infobase[lang+job+care+food] = []

    for echinfo in info:
        nowinfolst = echinfo.split()
        for lang in [nowinfolst[0], '-']:
            for job in [nowinfolst[1], '-']:
                for care in [nowinfolst[2], '-']:
                    for food in [nowinfolst[3], '-']:
                        infobase[lang+job+care+food].append(int(nowinfolst[-1]))
                        
    for key in infobase.keys():
        infobase[key].sort()

    for echquery in query:
        nowquery = echquery.replace(" and ", "")
        nowquerylst = nowquery.split()
        critquery = nowquerylst[0]
        critscore = int(nowquerylst[-1])

        scorelst = infobase[critquery]
        lft, rgt, tmp = 0, len(scorelst)-1, len(scorelst)
        while lft <= rgt:
            mid = (lft+rgt)//2
            if critscore <= scorelst[mid]:
                tmp = mid
                rgt = mid-1
            else:
                lft = mid+1

        answer.append(len(scorelst) - tmp)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# info = ["java backend junior pizza 150","python frontend senior chicken 210"]
query = ["java and backend and junior and - 100", "- and - and - and - 100"]
print(solution(info, query))

"""
# 2차 시도: for문 전체를 경우를 나눠서 데이터 저장.
infobase = [['cpp', 'java', 'python', '-'],
            ['backend', 'frontend', '-'],
            ['junior', 'senior', '-'],
            ['chicken', 'pizza', '-']]


def solution(info, query):
    answer = []
    infohit = [[[[[] for _ in range(3)] for _ in range(3)]
        for _ in range(3)] for _ in range(4)]

    for eachinfo in info:
        tmpinfo = eachinfo.split()
        tmpstr = tmpinfo.pop(-1)
        tmpinfo.extend(tmpstr.split(' '))
        idxs = [set([infobase[i].index(tmpinfo[i])]) for i in range(4)]
        for idx in idxs:
            idx.add(-1)
        for i0 in idxs[0]:
            for i1 in idxs[1]:
                for i2 in idxs[2]:
                    for i3 in idxs[3]:
                        infohit[i0][i1][i2][i3].append(int(tmpinfo[-1]))

    for i0 in range(4):
        for i1 in range(3):
            for i2 in range(3):
                for i3 in range(3):
                    infohit[i0][i1][i2][i3] =\
                        sorted(infohit[i0][i1][i2][i3],reverse=True)

    for eachquery in query:
        tmpquery = eachquery.split(' and ')
        tmpstr = tmpquery.pop(-1)
        tmpquery.extend(tmpstr.split(' '))
        i_s = [infobase[i].index(tmpquery[i]) for i in range(4)]
        tmplst = infohit[i_s[0]][i_s[1]][i_s[2]][i_s[3]]
        tmpans, tmpnum = 0, int(tmpquery[-1])
        for idx in range(len(tmplst)):
            if tmplst[idx] < tmpnum:
                break
            tmpans += 1
        answer.append(tmpans)

    return answer
"""


"""
# 1차 시도: 그때그때 쌩으로 조회하는 방식
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
    newquer = quer.split(' and ')
    tmpstr = newquer.pop(-1)
    newquer.extend(tmpstr.split(' '))
    for inf in info:
        newinf = inf.split()
        if ismatchquerinf(newinf, newquer):
            cnt += 1
    return cnt


def solution(info, query):
    answer = []
    for quer in query:
        answer.append(chkquer(info, quer))

    return answer
"""