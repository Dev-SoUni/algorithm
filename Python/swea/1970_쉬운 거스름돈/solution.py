import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    money_case = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0,
    }
    money = int(input())

    for case in money_case:
        if money/case > 0:
            money_case[case] = int(money/case)
            money %= case

    print(f"#{test_case}")
    #
    # for key in money_case:
    #     print(money_case[key], end=" ")
    # print()

    print(money_case.values())