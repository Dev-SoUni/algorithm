def solution(numbers):
    s_numbers = sorted(numbers, key= lambda x: str(x)*3, reverse = True)
    answer = ''.join(map(str, s_numbers))
    return answer if int(answer) != 0 else '0'