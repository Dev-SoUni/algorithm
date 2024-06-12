def solution(priorities, location):
    priorities = [[i, p] for i, p in enumerate(priorities)]
    process = []

    while priorities:
        item = priorities.pop(0)
        arr = [p for p in priorities if p[1] > item[1]]

        if arr:
            priorities.append(item)
        else:
            process.append(item)

    for i, p in enumerate(process):
        if p[0] == location:
            return i + 1


def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer