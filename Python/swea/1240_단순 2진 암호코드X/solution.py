import sys
sys.stdin = open("./input.txt", "r")

password_code = [
    [3, 2, 1, 1],
    [2, 2, 2, 1],
    [2, 1, 2, 2],
    [1, 4, 1, 1],
    [1, 1, 3, 2],
    [1, 2, 3, 1],
    [1, 1, 1, 4],
    [1, 3, 1, 2],
    [1, 2, 1, 3],
    [3, 1, 1, 2]
]

# 같은 값이 5 이상이면 다 짜르고
def conn_num(code):
    global M
    it_num_arr = []

    for c in range(0, M, 7):
        it = code[c:c+7]
        start_it = 0
        count = 0
        it_num_arr = [0 for _ in range(6)]

        print(it)
        if 1 not in it:
            print(it)
            continue

        for i in it:
            if it == start_it:
                count += 1
            else:
                start_it = it
                it_num_arr.append(count)
                count = 0

    return password_code.index(it_num_arr)

for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    code_map = [list(map(int, input())) for _ in range(N)]
    extra_code_map = []

    for code in code_map:
        if 1 in code:
            extra_code_map.append(conn_num(code))


    print(f"#{test_case} {N} {M}")
    print(extra_code_map)