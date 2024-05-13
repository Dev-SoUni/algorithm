import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    S, K = input().split()
    if S == "o..":
        S = 0
    elif S == ".o.":
        S = 1
    else:
        S = 2

    K = int(K)

    while K > 0:
        K -= 1
        if S != 0:
            S -= 1
        else:
            S = 1

    print(f"#{test_case} {S}")

