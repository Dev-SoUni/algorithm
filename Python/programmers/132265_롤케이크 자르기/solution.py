from collections import Counter

def solution(topping):
    answer = 0
    cake_one = Counter(topping)
    cake_two = set()

    for t in topping:
        cake_one[t] -= 1
        cake_two.add(t)

        if cake_one[t] == 0:
            cake_one.pop(t)

        if len(cake_one) == len(cake_two):
            answer += 1

    return answer