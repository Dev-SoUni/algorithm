def solution(want, number, discount):
    answer = 0
    for l in range(len(discount)-9):
        items = discount[l:l+10]
        items_dic = {}
        for it in items:
            if it not in items_dic:
                items_dic[it] = 1
            else:
                items_dic[it] += 1

        for i in range(len(want)):
            if want[i] not in items_dic or items_dic[want[i]] < number[i]:
                break
            if i == len(want) - 1:
                answer += 1

    return answer

from collections import Counter
def solution2(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]):
            answer += 1

    return answer