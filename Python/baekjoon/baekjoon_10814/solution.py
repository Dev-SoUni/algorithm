test_case = input()
info = list()
for i in range(0, int(test_case)):
    info.append(input())

info.sort()
print(info)

def solution(data):
    return data.sort()
    # if len(data) <= 1:
    #     return data
    #
    # pivot = data[0]
    # left = list()
    # right = list()
    #
    # for i in range(1, len(data)):
    #     if pivot[0] > data[i][0]:
    #         left.append(data[i])
    #     else:
    #         right.append(data[i])
    #
    # return solution(left) + [pivot] + solution(right)




# answer = solution(info)
# for i in range(0, len(answer)):
#     print(answer[i][0] + " " + answer[i][1])
