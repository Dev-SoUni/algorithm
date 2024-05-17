import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    T = int(input())
    total_distance = 0
    total_speed = 0

    for _ in range(T):
        info = list(map(int, input().split()))
        degree = info[0]
        distance = 1

        if len(info) > 1:
            distance = info[1]

        if degree == 1:
            total_speed += distance
        elif degree == 2:
            if total_speed < distance:
                total_speed = 0
            else:
                total_speed -= distance

        total_distance += total_speed

    print(f"#{test_case} {total_distance}")