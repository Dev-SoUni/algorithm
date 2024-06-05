n = 1260
coins = [500, 100, 50, 10]

def solution(n):
    count = 0
    for c in coins:
        count += n//c
        n %= c
    return count

answer = solution(n)
print(answer)
