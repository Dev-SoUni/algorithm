import sys
sys.stdin = open("./input.txt", "r")

for test_case in range(1, int(input()) + 1):
    h_one, m_one, h_two, m_two = map(int, input().split())

    h_sum = h_one + h_two
    m_sum = m_one + m_two

    if m_sum > 59:
        h_sum += 1
        m_sum -= 60

    if h_sum > 12:
        h_sum -= 12

    print(f"#{test_case} {h_sum} {m_sum}")
