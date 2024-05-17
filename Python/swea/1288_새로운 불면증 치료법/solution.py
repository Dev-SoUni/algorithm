import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    view = 1
    number = [0 for _ in range(10)]

    while 0 in number:
        view_number = N * view
        view += 1
        view_numbers = list(str(view_number))

        for v in view_numbers:
            number[int(v)] = 1

    print(f"#{test_case} {view_number}")
