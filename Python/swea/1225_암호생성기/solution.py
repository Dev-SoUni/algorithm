import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, 11):
    _ = input()
    code = list(map(int, input().split()))
    dec = 0

    while True:
        dec += 1
        if dec > 5:
            dec = 1

        item = code.pop(0) - dec
        if item <= 0:
            code.append(0)
            break
        code.append(item)

    print(f"#{test_case}", end=" ")
    print(*code)

