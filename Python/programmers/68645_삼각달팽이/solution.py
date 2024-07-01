def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]
    r = [1, 0, -1]
    c = [0, 1, -1]

    dir = 0
    c_r = 0
    c_c = 0

    num = sum([n for n in range(1, n + 1)])

    # num 숫자
    for i in range(1, num + 1):
        answer[c_r][c_c] = i

        next_r = c_r + r[dir]
        next_c = c_c + c[dir]

        if next_r >= n or next_c >= len(answer[next_r]) or answer[next_r][next_c] != 0:

            dir = (dir + 1) % 3
            # 0 1 2
            c_r += r[dir]
            c_c += c[dir]
        else:
            c_r = next_r
            c_c = next_c

    result = []
    for i in answer:
        for j in i:
            result.append(j)

    return result