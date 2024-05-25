def solution(keymap, targets):
    result = []

    for target in targets:
        count = 0
        for t in target:
            min_idx = 101

            for k in keymap:
                if t in k:
                    min_idx = min(min_idx, k.index(t)+1)

            if min_idx == 101:
                count = -1
                break

            count += min_idx

        result.append(count)

    return result
