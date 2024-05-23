import copy
import collections


def is_change(one, two):
    count = 0

    if one == two:
        return False

    for i in range(len(one)):
        if one[i] != two[i]:
            count += 1

        if count > 1:
            return False

    return True


def solution(begin, target, words):
    q = collections.deque()

    q.append((begin, 0, []))

    while len(q) > 0:
        current_word, current_count, current_visited = q.popleft()

        copied_current_visited = copy.copy(current_visited)

        if current_word == target:
            return current_count

        for word in words:
            if word not in copied_current_visited and is_change(current_word, word):
                copied_current_visited.append(word)
                q.append((word, current_count + 1, copied_current_visited))

    return 0