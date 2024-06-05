N = 17
K = 4

def solution(n, k):
    answer = 0
    while n != 1:
        answer += 1
        if n%k == 0:
            n = n//k
        else:
            n -= 1
    return answer

answer = solution(N, K)
print(answer)

# 답안 예시
def solution2(n, k):
    result = 0

    while True:
        # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
        target = (n//k)*k
        result += (n - target)
        n = target

        # N이 K보다 작을 때 탈출
        if n < k:
            break
        result += 1
        n //= k
    return result