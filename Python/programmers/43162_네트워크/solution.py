import collections

def solution(n, computers):
    count = 0
    visited = [False for _ in range(n)]
    q = collections.deque()

    while False in visited:
        q.append(visited.index(False))
        while q:
            i = q.popleft()
            visited[i] = True

            for j in range(n):
                if not visited[j] and j != i  and computers[i][j] == 1:
                    q.append(j)

        count += 1

    return count