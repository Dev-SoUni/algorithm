def solution(routes):
    routes.sort(key=lambda x: x[1])
    prev_end = routes[0][1]
    answer = 1

    for start, end in routes:
        if start > prev_end:
            prev_end = end
            answer += 1
    return answer