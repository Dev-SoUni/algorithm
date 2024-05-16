import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N = int(input())
    answer = [[0 for _ in range(N)] for _ in range(N)]
    arr = [list(map(str, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0:
                str = ""
                for w in range(N-1, -1, -1):
                    str += arr[w][j]
                answer[j][i] = str
            else:
                answer[j][i] = answer[j][i-1]



    print(f"#{test_case}")
    print(arr)
    print(answer)
