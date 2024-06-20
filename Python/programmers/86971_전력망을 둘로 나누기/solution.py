from collections import deque


def solution(n, wires):
    answer = float("inf")

    # 그래프 생성
    g = {}

    for w1, w2 in wires:
        if w1 not in g:
            g[w1] = []
        if w2 not in g:
            g[w2] = []

        g[w1].append(w2)
        g[w2].append(w1)

    # BFS
    for w1, w2 in wires:

        q = deque()
        q.append(1)
        check_list = [0] * n

        while q:
            start_node = q.popleft()
            check_list[start_node - 1] = 1

            for target in g[start_node]:
                if (start_node == w1 and target == w2) or (start_node == w2 and target == w1):
                    continue

                if check_list[target - 1] == 1:
                    continue

                q.append(target)

        count_one = check_list.count(1)
        count_zero = n - count_one
        answer = min(answer, abs(count_one - count_zero))

    return answer