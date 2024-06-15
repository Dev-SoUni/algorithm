def solution(participant, completion):
    p_dic = {}
    for p in participant:
        p_dic[p] = p_dic.get(p, 0) + 1

    for c in completion:
        p_dic[c] -= 1

    result = [k for k, v in p_dic.items() if v > 0]
    return result[0]