import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, 11):
    _ = input()
    SIZE = 100
    table = [list(map(int, input().split())) for _ in range(SIZE)]
    sum_arr = []

    # 가로
    for row in table:
        sum_arr.append(sum(row))

    # 세로
    for cell in range(SIZE):
        sum_length = 0
        for row in range(SIZE):
            sum_length += table[row][cell]
        sum_arr.append(sum_length)

    # 대각선
    sum_diagonal = 0
    sum_diagonal_reverse = 0
    for idx in range(SIZE):
        sum_diagonal += table[idx][idx]
        sum_diagonal_reverse += table[SIZE - idx - 1][SIZE - idx - 1]

    sum_arr.append(sum_diagonal)
    sum_arr.append(sum_diagonal_reverse)

    max_sum = max(sum_arr)
    print(f"#{test_case} {max_sum}")
