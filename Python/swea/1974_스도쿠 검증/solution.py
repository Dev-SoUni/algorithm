import sys
sys.stdin = open("./input.txt", "r")


def extract_square(board, start_row_index, start_col_index):
    arr = []
    for row in range(0, 3):
        for col in range(0, 3):
            arr.append(board[start_row_index + row][start_col_index + col])
    return arr


def solution():
    for test_case in range(1, int(input()) + 1):

        # print(f"#{test_case}")
        arr = []
        result = True

        # 데이터 생성
        for c in range(0, 9):
            rows = list(map(int, input().split()))
            arr.append(rows)

        # print(f'arr {arr}')
        # 가로 검증
        for row in arr:
            # print(f'row {row}')
            arr_handle = [0 for _ in range(0, 9)]
            for it in row:
                arr_handle[it-1] += 1
            # print(f'arr_handle {arr_handle}')
            if 0 in arr_handle:
                # print(f"horizon fail => {row}")
                result = False
                break

        if not result:
            print(f"#{test_case} 0")
            continue

        # 세로 검증
        for r in range(0,9):
            arr_handle = [0 for _ in range(0, 9)]
            for c in range(0,9):
                idx = arr[c][r]
                arr_handle[idx-1] += 1
            if 0 in arr_handle:
                # print(f"vertical fail")
                result = False
                break

        if not result:
            print(f"#{test_case} 0")
            continue

        # 정사각형 검증
        for row in (0, 3, 6):
            for col in (0, 3, 6):
                square = extract_square(arr, row, col)
                # print(f"square {square}")

                arr_handle = [0 for _ in range(0, 9)]
                for it in square:
                    arr_handle[it-1] += 1

                if 0 in arr_handle:
                    result = False
                    break

        if not result:
            print(f"#{test_case} 0")
            continue


        print(f"#{test_case} 1")

solution()
