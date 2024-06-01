def solution(n):
    answer = n
    bynary = format(n, "b")
    c_bynary = bynary.count("1")

    while True:
        answer += 1
        answer_bynary = format(answer, "b")
        c_answer_bynary = answer_bynary.count("1")
        if c_bynary == c_answer_bynary:
            return answer