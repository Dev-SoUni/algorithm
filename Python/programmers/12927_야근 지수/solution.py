from heapq import heappush, heappop

def solution(n, works):
    pq = []

    for work in works:
        heappush(pq, (-work, work))

    while n > 0:
        idx, val = heappop(pq)
        val -= 1
        if val <= 0:
            val = 0
        heappush(pq, (-val, val))
        n -= 1

    return sum([p[1]**2 for p in pq])
