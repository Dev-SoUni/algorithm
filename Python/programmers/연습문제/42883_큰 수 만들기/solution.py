def solution(number, k):
    answer = []
    for i in number:
        while answer and k > 0 and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)
    return ''.join(answer[:len(answer) - k])


def solution2(people, limit):
    people.sort()
    answer = 0
    while people:
        print(people)
        if people[0] + people[-1] <= limit:
            people.pop(0)

        answer += 1
        people.pop()
        print(f"people {people}")

    return answer

an = solution2([70, 50, 80, 50], 100)
