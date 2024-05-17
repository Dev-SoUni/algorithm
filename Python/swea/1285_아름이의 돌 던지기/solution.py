import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int((input())) + 1):
    N = int(input())
    locations = list(map(int, input().split()))
    min_location = abs(locations.pop())
    min_count = 1

    while locations:
        location = abs(locations.pop())
        if location < min_location:
            min_count = 1
            min_location = location
        elif location == min_location:
            min_count += 1

    print(f"#{test_case} {min_location} {min_count}")