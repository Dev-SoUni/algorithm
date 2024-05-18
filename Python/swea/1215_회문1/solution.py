import sys
sys.stdin = open("./input.txt", "r")

table_len = 8

for test_case in range(1, 11):
    text_len = int(input())
    text_table = [list(input()) for _ in range(8)]
    answer = 0

    for row in range(table_len):
        for j in range(0, table_len - text_len + 1):
            if text_table[row][j] == text_table[row][j+text_len-1]:
                item = text_table[row][j:j+text_len]
                reversed_item = list(reversed(item))
                if item == reversed_item:
                    answer += 1

    for col in range(table_len):
        for j in range(0, table_len - text_len + 1):
            if text_table[j][col] == text_table[j+text_len-1][col]:
                item_1 = []
                for i in range(j, j+text_len):
                    item_1.append(text_table[i][col])
                reversed_item_1 = list(reversed(item_1))

                if item_1 == reversed_item_1:
                    answer += 1

    print(f"#{test_case} {answer}")
