import math

def solution(n, stations, w):
    answer = 0
    wid = (w * 2) + 1
    l = len(stations)
    for i in range(l + 1):
        if i == 0:
            remain = stations[i] - w - 1
        elif i == l:
            remain = n - stations[-1] - w
            if remain <= 0: break
        else:
            remain = stations[i] - 1 - w - stations[i - 1] - w
        answer += math.ceil(remain / wid)

    return answer

