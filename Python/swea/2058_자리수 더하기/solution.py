import sys
sys.stdin = open("./input.txt", "r")

numbers = input()

answer = 0

for number in numbers:
    answer += int(number)

print(answer)