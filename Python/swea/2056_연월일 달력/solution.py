import sys
sys.stdin = open("./input.txt", "r")

max_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, int(input()) + 1):
    answer = 0
    day = input()
    year = day[0:4]
    month = int(day[4:6])
    date = int(day[6:8])

    if month <= 0 or month > 13:
        answer = -1
    else:
        if date > max_date[month - 1]:
            answer = -1
        else:
            answer = str(year) + "/" + day[4:6] + "/" + day[6:8]
    print(f"#{test_case} {answer}")