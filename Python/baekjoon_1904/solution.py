def solution(n):
    data = [0] * max(3, n+1)
    data[1] = 1
    data[2] = 2
    for i in range(3, n+1):
        data[i] = (data[i-1] + data[i-2])%15746

    return data[n]

result = solution(int(input()))
print(result)