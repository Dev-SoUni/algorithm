import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, 11):
    _ = input()
    WORD_LENGTH = 100
    word_map = [list(input()) for _ in range(WORD_LENGTH)]
    max_length = 0

    # 가로
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            for length in range(WORD_LENGTH, 0, -1):
                if j + length <= WORD_LENGTH:
                    if word_map[i][j:j+length] == word_map[i][j:j+length][::-1]:
                        max_length = max(max_length, length)

    # 세로
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            for length in range(WORD_LENGTH, 0, -1):
                if j + length <= WORD_LENGTH:
                    if [word_map[k][i] for k in range(j, j + length)] == [word_map[k][i] for k in range(j, j + length)][::-1]:
                        max_length = max(max_length, length)

    print(f"#{test_case} {max_length}")
