import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    while heap[0] < K:
        if len(heap) < 2:
            return -1

        answer += 1
        it = heapq.heappop(heap) + (heapq.heappop(heap) * 2)
        heapq.heappush(heap, it)

    return answer