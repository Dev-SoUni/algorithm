import copy

def solution(sizes):
    w = 0
    h = 0

    _sizes1 = copy.deepcopy(sizes)
    for size in _sizes1:
        size.append(w)
        w = max(size)

    _sizes2 = copy.deepcopy(sizes)
    for size in _sizes2:
        it = min(size)
        h = max([it, h])

    return w * h

def solution2(sizes):
    return max(max(size) for size in sizes) * max(min(size) for size in sizes)
