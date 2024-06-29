def solution(elements):
    answer = set()

    for r in range(1, len(elements) + 1):
        for s in range(len(elements)):
            start = s
            end = (s + r) % len(elements)
            if end > start:
                answer.add(sum(elements[start:end]))
            else:
                answer.add(sum(elements[start:] + elements[:end]))

    return len(answer)
