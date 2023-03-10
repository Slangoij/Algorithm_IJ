def strip_lst(s):
    tmp_s = s[1:-1].split('}')[:-1]
    return list(map(lambda x: x.strip(',{'), tmp_s))

def solution(s):
    s_str_lst = strip_lst(s)

    answer = [ set(s_str_lst[0].split(',')) ]
    for itm in s_str_lst[1:]:
        answer.append((set(itm.split(',')) - answer[-1]).pop())

    return list(map(lambda x: list(x)[0], answer))


if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))