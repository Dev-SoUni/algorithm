
import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    case_num = int(input())
    case = list(map(int, input().split()))
    max_item = case.pop()
    result = 0

    while case:
        item = case.pop()
        if max_item < item:
            max_item = item
        else:
            result += max_item - item

    print("#"+str(test_case) + " " + str(result))
