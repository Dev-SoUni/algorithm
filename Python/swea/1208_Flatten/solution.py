import sys
sys.stdin = open("./input.txt", "r")

def act_dump():
    sorted_boxs = sorted(boxs)
    sorted_boxs[0] += 1
    sorted_boxs[-1] -= 1
    return sorted_boxs


for test_case in range(1, 11):
    dump = int(input())
    boxs = list(map(int, input().split()))

    for act in range(dump):
        boxs = act_dump()
    boxs = sorted(boxs)

    answer = boxs[-1] - boxs[0]

    print(f"#{test_case} {answer}")
