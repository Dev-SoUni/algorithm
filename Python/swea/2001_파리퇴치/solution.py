import sys

sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    # 전체 배열 생성
    arr = []
    for i in range(0, N):
        arr.append(list(map(int, input().split())))

    # 최대값 구하기
    max_count = 0
    for col in range(0, N - (M - 1)):
        for row in range(0, N - (M - 1)):

            start = [col, row]
            temp = 0

            for i in range(0, M):
                for j in range(0, M):
                    temp += arr[start[0] + i][start[1] + j]

            if temp > max_count:
                max_count = temp

    print(f"#{test_case} {max_count}")

