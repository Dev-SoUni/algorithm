import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    s = []
    k = []

    def dfs(i, taste, kcal):
        global max_taste
        if kcal > L:
            return
        if taste > max_taste:
            max_taste = taste
        if i == N:
            return
        dfs(i+1, taste + s[i], kcal + k[i])
        dfs(i+1, taste, kcal)


    for _ in range(N):
        score, kcal = map(int, input().split())
        s.append(score)
        k.append(kcal)

    max_taste = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {max_taste}")