import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for cell in range(N):
        it = 0
        for row in range(N):
            if it == 1 and table[row][cell] == 2:
                it = 0
                count += 1
            elif table[row][cell] == 1:
                it = table[row][cell]

    print(f"#{test_case} {count}")