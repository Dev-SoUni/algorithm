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


# 참고 풀이
def solution2(n, stations, w):
    answer = 0
    range = w + w + 1

    now = 1
    for station in stations:
        length = station - w - now
        if length > 0:
            answer += math.ceil(length / range)
        now = station + w + 1

    if n >= now:
        answer += math.ceil((n - now + 1) / range)

    return answer