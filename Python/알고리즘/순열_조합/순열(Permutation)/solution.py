# 1. DFS를 이용
# 2. 체크리스트, 공유된 자원 이용

def permutation(n, r):
    answer = []

    def generate(choose, checklist):
        if len(choose) == r:
            answer.append(choose.copy())
            return

        for i in range(len(n)):
            if checklist[i] == 0:
                choose.append(n[i])
                checklist[i] = 1
                generate(choose, checklist)
                choose.pop()
                checklist[i] = 0

    generate([], [0] * len(n))

    return answer


result = permutation([1, 2, 3], 2)
print(result)