def solution(people, limit):
    boat = 0
    people.sort()
    left_idx = 0
    right_idx = len(people) - 1

    while left_idx <= right_idx:

        if people[left_idx] + people[right_idx] > limit:
            boat += 1
            right_idx -= 1
        else:
            boat += 1
            left_idx += 1
            right_idx -= 1

    return boat