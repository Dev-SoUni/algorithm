import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    text = input()
    print(f"#{test_case}")
    print(text)