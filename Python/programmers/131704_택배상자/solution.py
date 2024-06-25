from collections import deque

def solution(order):
    l = len(order)
    order = deque(order)
    container = deque()

    for i in range(1, l + 1):
        if order[0] != i:
            deque.append(container, i)
        else:
            deque.popleft(order)

        while container and order[0] == container[-1]:
            deque.popleft(order)
            container.pop()

    return l - len(container)