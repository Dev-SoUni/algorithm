import sys
sys.stdin = open("./input.txt", "r")



for test_case in range(1, int(input()) + 1):
    num = int(input())
    cal_arr = {
        2: 0,
        3: 0,
        5: 0,
        7: 0,
        11: 0
    }

    for cal in cal_arr:
        while True:
            if num%cal == 0:
                cal_arr[cal] += 1
                num = num//cal
            else:
                break

    print(f"#{test_case}", end=" ")
    print(*cal_arr.values(), end="\n")