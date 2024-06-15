def solution(clothes):
    answer = 1
    d_c = {}

    # 같은 종류를 한 배열에 넣음
    for clothe, category in clothes:
        if category not in d_c:
            d_c[category] = [clothe]
        else:
            d_c[category].append(clothe)

    for d in d_c:
        answer *= len(d_c[d]) + 1
        print(answer)

    return answer - 1
