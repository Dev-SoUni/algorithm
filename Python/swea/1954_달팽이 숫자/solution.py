
import sys
sys.stdin = open("./input.txt", "r")

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print("#" + str(test_case))
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    move = 0
    i, j = 0, 0

    for k in range(1, N * N + 1):
        snail[i][j] = k
        mi = i + di[move]
        mj = j + dj[move]

        if 0 <= mi < N and 0 <= mj < N and snail[mi][mj] == 0:
            i, j = mi, mj
        else:
            move = (move + 1) % 4
            i = i + di[move]
            j = j + dj[move]

    for x in snail:
        print(*x)
