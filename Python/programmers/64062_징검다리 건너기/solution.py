import heapq

def solution(stones, k):
    answer = 0
    heapq.heappush()

    while True:
        answer += 1

        stones = [s - 1 if s > 0 else s for s in stones]
        print(stones)
        count = 0
        for s in stones:
            if s == 0:
                count += 1
            else:
                count = 0

            if count >= k:
                return answer

    # return answer


an = solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
print(an)
