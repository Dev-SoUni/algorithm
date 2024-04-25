def solution():
    test_case = int(input())
    dance = ["ChongChong"]

    for i in range(0, test_case):
        person = input().split(" ")
        isDance = [item for item in person if item in dance]
        if isDance:
            dance = dance + person

    dance = list(set(dance))
    return len(dance)

answer = solution()
print(answer)
