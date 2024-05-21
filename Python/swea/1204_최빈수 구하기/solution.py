import sys
sys.stdin = open("./input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    input()

    scores = list(map(int, input().split()))
    score_data = dict()

    for score in scores:
        if score in score_data:
            score_data[score] += 1
        else:
            score_data[score] = 1

    sorted_score_data = sorted(score_data.items(), key=lambda x:x[1], reverse=True)
    print("#" + str(test_case) + " " + str(sorted_score_data.pop(0)[0]))