import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    _ = input()
    score_list = list(map(int, input().split()))
    score_arr = [0] * 101
    mode = 0

    for score in score_list:
        score_arr[score] += 1
        if score_arr[mode] <= score_arr[score]:
            mode = score

    print(f"#{test_case} {mode}")
