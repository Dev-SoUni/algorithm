def combination(n, r):
    answer = []

    def generation(choose, begin):
        if len(choose) == r:
            answer.append(choose.copy())

        for i in range(begin, len(n)):
            choose.append(n[i])
            begin = i + 1
            generation(choose, begin)
            choose.pop()

    generation([], 0)
    return answer

result = combination([1, 2, 3, 4, 5], 2)
print(result)