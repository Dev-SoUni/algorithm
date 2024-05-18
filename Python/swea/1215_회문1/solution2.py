import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, 11):
    MAP_SIZE = 8
    word_length = int(input())
    word_map = [list(input()) for _ in range(MAP_SIZE)]
    count = 0

    # 가로
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE - word_length + 1):
            if word_map[i][j:j + word_length] == word_map[i][j:j + word_length][::-1]:
                count += 1

    # 세로
    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE - word_length + 1):
            if [word_map[k][i] for k in range(j, j + word_length)] == [word_map[k][i] for k in range(j, j + word_length)][::-1]:
                count += 1

    print(f"#{test_case} {count}")
