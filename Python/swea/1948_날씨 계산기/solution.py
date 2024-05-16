import sys
sys.stdin = open("./input.txt", "r")

day_end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, int(input()) + 1):
    one_month, one_day, two_month, two_day = map(int, input().split())
    result = 0

    for month in range(one_month-1, two_month):
        if month == one_month-1:
            result += day_end[month] - one_day + 1
        elif month == two_month-1:
            result += two_day
        else:
            result += day_end[month]

    print(f"#{test_case} {result}")
