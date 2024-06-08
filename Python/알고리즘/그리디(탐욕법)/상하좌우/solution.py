import sys
sys.stdin = open("./input.txt", "r")


def solution():
    N = int(input())
    plan = input().split()
    dic = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1,0]}
    i, j = 1, 1

    for p in plan:
        p1, p2 = dic[p]
        mi, mj = i + p1, j + p2
        if 1 <= mi <= N and 1 <= mj <= N:
            i, j = mi, mj

    print(i, j)

solution()
