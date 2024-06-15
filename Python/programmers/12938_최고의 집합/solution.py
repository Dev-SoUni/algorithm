def solution(n, s):
    mid = int(s/n)
    if mid < 1:
        return [-1]

    answer = [mid for _ in range(n)]
    answer_sum = sum(answer)

    i = n-1
    while answer_sum != s:
        answer[i] += 1
        answer_sum += 1
        i -= 1

    return answer