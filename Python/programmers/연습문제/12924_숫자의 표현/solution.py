def solution(n):
    answer = 0
    start_num = 0

    while start_num <= n:
        start_num += 1
        hab = 0
        increa_num = start_num

        while hab < n:
            hab += increa_num
            if hab == n:
                answer += 1
            increa_num += 1

    return answer