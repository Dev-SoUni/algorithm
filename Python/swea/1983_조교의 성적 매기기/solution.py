import sys
sys.stdin = open("./input.txt", "r")

def total_score(num):
    middle, final, work = map(int, input().split())
    score = (middle * 0.35) + (final * 0.45) + (work * 0.2)
    score_arr[num] = score

for test_case in range(1, int(input()) + 1):
    answer = ""
    N, K = map(int, input().split())
    score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    score_arr = {}

    for num in range(1, N + 1):
        total_score(num)
    score_arr = sorted(score_arr.items(), key=lambda item: item[1], reverse=True)

    skip = N/10
    score_idx = 0

    for s in range(0, len(score_arr) + 1):
        if s % skip == 0:
            score_idx += 1

        if score_arr[s][0] == K:
            answer = score[score_idx-1]
            break

    print(f"#{test_case} {answer}")