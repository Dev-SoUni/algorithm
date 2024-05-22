from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            m_x = x + dx[i]
            m_y = y + dy[i]
            if 0 <= m_x < n and 0 <= m_y < m and maps[m_x][m_y] == 1:
                maps[m_x][m_y] = maps[x][y] + 1
                q.append((m_x, m_y))

    if maps[n - 1][m - 1] == 1:
        return -1
    return maps[n - 1][m - 1]
