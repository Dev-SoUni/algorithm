def solution(name, yearning, photo):
    answer = []
    for p in photo:
        score = 0
        for person in p:
            if person not in name:
                continue
            score += yearning[name.index(person)]

        answer.append(score)
    return answer