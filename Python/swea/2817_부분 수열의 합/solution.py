import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    case_cnt = 0

    def dfs(i, current_sum):
        global case_cnt

        if current_sum == K:
            case_cnt += 1
            return
        if i == N:
            return

        dfs(i+1, current_sum + A[i])
        dfs(i+1, current_sum)

    dfs(0, 0)

    print(f"#{test_case} {case_cnt}")
