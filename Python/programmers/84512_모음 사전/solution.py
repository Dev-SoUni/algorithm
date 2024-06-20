from collections import deque


next_chars = {"A": "E", "E": "I", "I": "O", "O": "U", "U": "A"}


def solution(word):
    count = 1
    chars = deque(["A"])
    max_length = 5

    while word != "".join(chars):
        if len(chars) == max_length:
            while chars[-1] == "U":
                chars.pop()

            chars[-1] = next_chars[chars[-1]]
        else:
            chars.append("A")

        count += 1

    return count