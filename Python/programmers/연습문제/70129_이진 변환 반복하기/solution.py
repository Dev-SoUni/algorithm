from collections import Counter

def solution(s):
    i = 0
    zero_count = 0
    while s != "1":
        i += 1
        s_counter = Counter(s)
        zero_count += s_counter["0"]
        l = s_counter["1"]
        s = format(l, "b")

    return [i, zero_count]