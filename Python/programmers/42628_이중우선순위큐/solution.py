from heapq import heappush, heappop


def solution(operations):
    answer = []
    max_heap = []
    min_heap = []

    for operation in operations:
        oper, num = operation.split()
        num = int(num)

        if oper == "I":
            node = [num, True]
            heappush(max_heap, (-num, node))
            heappush(min_heap, (num, node))
        else:
            if num == 1:
                while len(max_heap) > 0:
                    num, node = heappop(max_heap)
                    val, vali = node
                    if vali:
                        node[1] = False
                        break

            elif num == -1:
                while len(min_heap) > 0:
                    num, node = heappop(min_heap)
                    val, vali = node
                    if vali:
                        node[1] = False
                        break

    while len(max_heap) > 0:
        num, node = heappop(max_heap)
        val, vali = node
        if vali:
            answer.append(val)
            break
    if len(answer) == 0:
        return [0, 0]

    while len(min_heap) > 0:
        num, node = heappop(min_heap)
        val, vali = node
        if vali:
            answer.append(val)
            break

    return answer
