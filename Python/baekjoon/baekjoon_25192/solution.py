def solution():
    test_case = int(input())

    result = 0
    people = {}

    for _ in (range(0, test_case)):
        person = input()
        if person == "ENTER":
            people = {}
        elif not person in people:
            people[person] = True
            result += 1

    return result


answer = solution()
print(answer)
