import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    number_arr = list(map(int, input().split()))
    number_arr.sort()

    print(f"#{test_case}", end=" ")
    print(*number_arr)