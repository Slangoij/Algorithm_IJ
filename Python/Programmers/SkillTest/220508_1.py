

def solution(genres, plays):
    answer = []

    gens = set(genres)
    gendict = {i:[] for i in gens}

    for idx, (gen, plycnt) in enumerate(zip(genres, plays)):
        gendict[gen].append((idx, plycnt))
    sortedlst = sorted(list(gendict.values()), key=lambda x: -sum(list(zip(*x))[1]))
    for eachgen in sortedlst:
        eachgen.sort(key=lambda x: -x[1])
        for i in range(min(2,len(eachgen))):
            answer.append(eachgen[i][0])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)