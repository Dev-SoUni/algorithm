def solution(numbers):
    answer = 0
    ans = []
    l = len(numbers)

    # 순열
    def generate(choose, check_list):
        if r == len(choose):
            ans.append(choose.copy())
            return

        for i in range(len(numbers)):
            if check_list[i] == 0:
                check_list[i] = 1
                choose.append(numbers[i])
                generate(choose, check_list)
                check_list[i] = 0
                choose.pop()

    for r in range(1, l + 1):
        generate([], [0] * l)

    ans = set([int(''.join(a)) for a in ans])

    # 소수 판별
    def is_prime_number(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    # 소수인지 판별
    for a in ans:
        if a != 0 and a != 1 and is_prime_number(a):
            answer += 1

    return answer

