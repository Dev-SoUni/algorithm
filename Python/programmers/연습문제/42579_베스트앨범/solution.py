def solution(genres, plays):
    answer = []
    p_d = {}
    s_sum_category = {}

    for i, g in enumerate(genres):
        if g not in p_d:
            p_d[g] = [[i, plays[i]]]
            s_sum_category[g] = plays[i]
        else:
            p_d[g].append([i, plays[i]])
            s_sum_category[g] += plays[i]
    s_sum_category = sorted(s_sum_category, key=lambda x:s_sum_category[x], reverse = True)

    for k in s_sum_category:
        item = p_d[k].copy()
        s_item = sorted(item, key=lambda x:x[1], reverse=True)
        count = 0

        for it in s_item:
            count += 1
            answer.append(it[0])
            if count == 2:
                break

    return answer