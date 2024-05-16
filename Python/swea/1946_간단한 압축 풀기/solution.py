import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    document = {}

    for _ in range(N):
        key, value = input().split()
        document[key] = int(value)

    count = 0
    print(f"#{test_case}")
    for key in document:
        item = document[key]
        for _ in range(item):
            count += 1
            print(key, end="")

            if count == 10:
                count = 0
                print()
    print()

