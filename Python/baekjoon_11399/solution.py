num = int(input())
time = list(map(int, input().split()))
time.sort()
result = [time[0]]


def solution():
    acc = result[0]
    for i in range(1, len(time)):
        result.append(result[i - 1] + time[i])
        acc += result[i]

    print(acc)


solution()
