def solution(n):
    dp = [0] * 101
    dp[1], dp[2], dp[3] = 1, 1, 1

    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]

    return dp[n]


case_count = int(input())

for i in range(1, case_count+1):
    answer = solution(int(input()))
    print(answer)