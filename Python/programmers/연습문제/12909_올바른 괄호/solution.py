from collections import deque


def solution(s):
    de_s = deque(s)
    stack = []

    while de_s:
        it = de_s.popleft()

        if stack and stack[-1] == "(" and it == ")":
            stack.pop()
        else:
            stack.append(it)

    return False if stack else True
