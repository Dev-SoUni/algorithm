def solution(operations):
    h = []

    for o in operations:
        g, n = o.split()
        if g == "I":
            h.append(int(n))
        elif h and n == "1":
            h.sort()
            h.pop()
        elif h and n == "-1":
            h.sort()
            h.pop(0)

    if not h:
        return [0, 0]
    return [max(h), min(h)]

