import sys
sys.stdin = open("./input.txt", "r")

def check_row():
    global answer
    for row in range(N):
        check = 0
        for cell in range(N):
            if puzzle[row][cell] == 1:
                check += 1
            else:
                check = 0

            if check == K:
                if (cell != N-1 and puzzle[row][cell+1] != 1) or cell == N-1:
                    answer += 1
                    check = 0

def check_cell():
    global answer
    for cell in range(N):
        check = 0
        for row in range(N):
            if puzzle[row][cell] == 1:
                check += 1
            else:
                check = 0

            if check == K:
                if (row != N-1 and puzzle[row+1][cell] != 1) or row == N-1:
                    answer += 1
                    check = 0


for test_case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    check_row()
    check_cell()

    print(f"#{test_case} {answer}")

