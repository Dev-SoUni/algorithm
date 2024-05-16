import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())

    board = [[0] * N for _ in range(N)]
    board[0][0] = 1

    for row in range(1, N):
        for cell in range(row + 1):
            if cell == 0 or cell == row:
                board[row][cell] = 1
            else:
                board[row][cell] = board[row-1][cell-1] +board[row-1][cell]

    print(f"#{test_case}")
    for i in board:
        for j in i:
            if j != 0:
                print(j, end=" ")
        print()
