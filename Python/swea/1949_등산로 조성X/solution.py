import sys
sys.stdin = open("./input.txt", "r")

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def search_start():
    max_start = []
    max_point = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == max_point:
                max_point = maps[i][j]
                max_start.append((i, j))
            elif maps[i][j] > max_point:
                max_point = maps[i][j]
                max_start.clear()
                max_start.append((i, j))
    return max_start

def search_direct(i ,j):
    if i == 0 or j == 0 or i == N-1 or j == N-1:
        return

    # for num in range(0, 5):
    #     if maps[i][j] > maps[i + di[num]][j + dj[num]]:


for test_case in range(1, int(input()) + 1):
    N, K = input().split()
    N = int(N)

    maps = [list(map(int, input().split())) for _ in range(N)]
    start_point = search_start()

    for point in start_point:
        print(point[0], point[1])

    print(f"#{test_case}")
    print(maps)
    print(start_point)
