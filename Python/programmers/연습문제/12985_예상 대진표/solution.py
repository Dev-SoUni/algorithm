def solution(n,a,b):
    answer = 0
    tone = []

    for i in range(1, n+1):
        if i == a or i == b:
            tone.append(True)
        else:
            tone.append(False)

    while True:
        answer += 1
        tone_wh = []
        for i in range(0, len(tone), 2):
            node1 = tone[i]
            node2 = tone[i+1]
            if node1 and node2:
                return answer
            tone_wh.append(node1 + node2)

        tone = tone_wh


def solution2(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        a = (a+1) // 2
        b = (b+1) // 2

    return answer