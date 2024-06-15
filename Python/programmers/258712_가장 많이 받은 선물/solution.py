def solution(friends, gifts):
    friend_dic = {}
    # 선물지수 (준선물 - 받은선물)
    gift_dic = {}

    answer_dic = {}

    for friend in friends:
        friend_dic[friend] = {}
        answer_dic[friend] = 0
        gift_dic[friend] = [0 for _ in range(3)]

    for f_d in friend_dic:
        for_count = 0
        for friend in friends:
            if f_d == friend:
                continue
            friend_dic[f_d][friend] = 0

    for gift in gifts:
        send, get = gift.split()
        friend_dic[send][get] += 1

    for key, value in friend_dic.items():
        count = 0
        for in_key, in_value in value.items():
            count += in_value
        gift_dic[key][0] = count

        send_count = 0
        for friend in friends:
            if key == friend:
                continue
            send_count += friend_dic[friend][key]
        gift_dic[key][1] = send_count

    for key, value in gift_dic.items():
        gift_dic[key][2] = value[0] - value[1]

    checked = []
    for key, value in friend_dic.items():
        for k, v in value.items():
            if k in checked:
                continue

            if v > friend_dic[k][key]:
                answer_dic[key] += 1
            elif v < friend_dic[k][key]:
                answer_dic[k] += 1

            elif gift_dic[key][2] > gift_dic[k][2]:
                answer_dic[key] += 1
            elif gift_dic[key][2] < gift_dic[k][2]:
                answer_dic[k] += 1

            checked.append(key)

    answer = 0
    for k, v in answer_dic.items():
        answer = max(answer, v)

    return answer
