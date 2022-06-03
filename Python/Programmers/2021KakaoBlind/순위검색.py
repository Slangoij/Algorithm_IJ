infobase = [{'cpp', 'java', 'python', '-'},
            {'backend', 'frontend', '-'},
            {'junior', 'senior', '-'},
            {'chicken', 'pizza', '-'}]


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