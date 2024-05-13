import sys
sys.stdin = open("./input.txt", "r")

sodoku = []


# 스도쿠 배열 생성
def create_sodoku():
    sodoku.clear()
    for i in range(0, 9):
        arr = list(map(int, input().split()))
        sodoku.append(arr)
    return sodoku

# 스토쿠 가로 검증
def verification_row():
    for row in sodoku:
        verification = [0 for _ in range(0, 9)]
        for it in row:
            verification[it-1] += 1
        if 0 in verification:
            return False

# 스토쿠 세로 검증
def verification_col():
    for col in range(0, 9):
        verification = [0 for _ in range(0, 9)]
        for row in range(0, 9):
            verification[sodoku[row][col]-1] += 1
        if 0 in verification:
            return False

# 스토쿠 3*3 사각형 검증
def verification_box():
    start = []
    for col in range(0, 7, 3):
        for row in range(0, 7, 3):
            start.append((col, row))

    for idx in start:
        verification = [0 for _ in range(0, 9)]

        for col in range(0, 3):
            for row in range(0, 3):
                c = idx[0] + col
                r = idx[1] + row
                verification[sodoku[c][r]-1] += 1
        if 0 in verification:
            return False


def solution():
    answer = 1
    # 스도쿠 배열 생성
    create_sodoku()

    # 스토쿠 가로, 세로 검증
    if verification_row() == False or verification_col() == False or verification_box() == False:
        answer = 0

    print(f"#{test_case} {answer}")


for test_case in range(1, int(input()) + 1):
    solution()
