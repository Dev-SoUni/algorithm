import sys
sys.stdin = open("./input.txt", "r")


def connect_node(cell, row):
    # row, cell 이 0, 6 이면 제외
    if cell == 0 or cell == end_node or row == 0 or row == end_node:
        node_case[(cell, row)] = []
    # 전선을 연결할때 노드 체크
    # 위, 오른쪽, 아래, 왼쪽
    else:
        node_case[(cell, row)] = [(0, row), (cell, end_node), (end_node, row), (cell, 0)]


def check_node(node):
    if len(node_case[node]) <= 0:
        return

    print(node_case.keys())
    for key in node_case.keys():
        for node in node_case:
            print((node[0] - key[0], node[1] - key[1]))



# for test_case in range(1, int(input()) + 1):
for test_case in range(1, int(input()) + 1):
    print(f"#{test_case} ")
    N = int(input())
    end_node = N -1
    processor = [list(map(int, input().split())) for _ in range(0, N)]
    node_case = {}

    for cell in range(0, N):
        for row in range(0, N):
            if processor[cell][row] == 1:
                connect_node(cell, row)
    print(node_case)

    for node in node_case:
        check_node(node)

    print(node_case)

