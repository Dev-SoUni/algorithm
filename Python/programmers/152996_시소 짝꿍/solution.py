distance_cal = [1, 2 / 3, 2 / 4, 3 / 4]


def solution(weights):
    count = 0
    weights.sort()
    weight_len = len(weights)

    for i in range(weight_len):
        for j in range(i + 1, weight_len):
            for c in distance_cal:
                if weights[i] == int(weights[j] * c):
                    count += 1
                    continue

    return count
