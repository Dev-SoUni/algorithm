import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, L = map(int, input().split())
    s = []
    k = []
    max_score = 0

    for _ in range(N):
        score, kcal = map(int, input().split())
        s.append(score)
        k.append(kcal)

    def dfs(i, score, kcal):
        global max_score

        if kcal > L:
            return
        if score > max_score:
            max_score = score
        if i == N:
            return

        dfs(i+1, score + s[i], kcal + k[i])
        dfs(i+1, score, kcal)

    dfs(0, 0, 0)

    print(f"#{test_case} {max_score}")