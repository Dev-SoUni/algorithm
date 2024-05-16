import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

# 3 + 30 - 21 = 12
# 6 - 35 + 15 = -14
# -7 + 25 + 12 = 30

def cal(big_arr, min_arr, gap):
    max_num = 0
    for i in range(gap):
        cal_num = 0
        # print(max_num)
        for num in range(len(min_arr)):
            cal_num += (min_arr[num] * big_arr[i + num])
        if cal_num > max_num:
            max_num = cal_num
    return max_num


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        result = cal(A, B, N - M + 1)
    else:
        result = cal(B, A, M - N + 1)
    print(f"#{test_case} {result}")