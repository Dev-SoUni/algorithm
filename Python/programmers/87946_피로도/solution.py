def permutation(n, r):
    ans = []

    def generate(choose, check_list):
        if len(choose) == r:
            ans.append(choose.copy())
            return

        for i in range(len(n)):
            if check_list[i] == 0:
                check_list[i] = 1
                choose.append(n[i])
                generate(choose, check_list)
                check_list[i] = 0
                choose.pop()

    generate([], [0] * len(n))

    return ans


def solution(k, dungeons):
    max_result = 0

    # 탐험 순서
    n = [i + 1 for i in range(len(dungeons))]
    cases = permutation(n, len(n))

    for i in range(len(cases)):
        case = cases[i]
        it_k = k
        res = 0

        for c in case:
            it = dungeons[c-1]
            if it_k >= it[0]:
                it_k -= it[1]
                res += 1
            else:
                break

        max_result = max(max_result, res)

    return max_result