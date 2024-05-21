import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, 11):
    _ = input()
    N, M = map(int, input().split())

    def go(n, m):
        if m == 1:
            return n
        else:
            return n * go(n, m - 1)

    answer = go(N, M)

    print(f"#{test_case} {answer}")
