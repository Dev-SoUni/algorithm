import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    P, Q, R, S, W = map(int, input().split())
    result = 0
    a = P * W

    b = Q
    if R < W:
        b += (W - R) * S

    if a < b:
        result = a
    else:
        result = b

    print(f"#{test_case} {result}")