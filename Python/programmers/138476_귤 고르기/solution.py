def solution(k, tangerine):
    tanger_dic = {}
    for t in tangerine:
        tanger_dic[t] = tanger_dic.get(t, 0) + 1

    sort_tanger_dic = sorted(tanger_dic.items(), key=lambda x:x[1], reverse=True)

    count = 0
    for ta in sort_tanger_dic:
        count += 1
        k -= ta[1]
        if k <= 0:
            break

    return count