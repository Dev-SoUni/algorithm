def combination(n, r):
    answer = []

    def generate(choose, begin):
        if len(choose) == r:
            answer.append(choose.copy())
            return

        for i in range(begin, len(n)):
            choose.append(n[i])
            generate(choose, i + 1)
            choose.pop()

    generate([], 0)
    return answer

result = combination([1, 2, 3, 4, 5], 2)
print(result)