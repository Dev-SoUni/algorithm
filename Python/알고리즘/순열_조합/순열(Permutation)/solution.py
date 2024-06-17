# 1. DFS를 이용
# 2. 체크리스트, 공유된 자원 이용

def perm(n, r):
    answer = []

    def gen(choose, checklist):
        if len(choose) == r:
            answer.append(choose.copy())
            return

        for i in range(len(n)):
            if checklist[i] == 0:
                choose.append(n[i])
                checklist[i] = 1
                gen(choose, checklist)
                choose.pop()
                checklist[i] = 0

    gen([], [0] * len(n))

    return answer


result = perm([1, 2, 3], 2)
print(result)