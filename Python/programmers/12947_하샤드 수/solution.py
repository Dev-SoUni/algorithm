def solution(x):
    sum_num = sum(map(int, list(str(x))))
    return x % sum_num == 0