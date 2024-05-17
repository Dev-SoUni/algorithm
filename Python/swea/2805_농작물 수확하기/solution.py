import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    answer = 0
    farm = [list(map(int, input())) for _ in range(N)]
    cell_mid = int(N / 2)
    gap = 0
    isIncrease = True

    for row in range(N):
        for it in farm[row][cell_mid-gap:cell_mid+gap+1]:
            answer += it

        if cell_mid + gap == N-1:
            isIncrease = False

        if isIncrease:
            gap += 1
        else:
            gap -= 1

    print(f"#{test_case} {answer}")