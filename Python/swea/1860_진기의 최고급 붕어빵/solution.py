import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    customer_times = list(map(int, input().split()))

    customer_times.sort()
    result = "Possible"

    current_fish = 0
    sell = 0

    for time in customer_times:
        current_fish = (time // M) * K
        sell += 1

        if sell > current_fish:
            result = "Impossible"
            break

    print(f"#{test_case} {result}")


