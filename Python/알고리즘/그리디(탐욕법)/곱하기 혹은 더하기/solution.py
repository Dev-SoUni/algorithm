# 숫자가 2이상이면 x, 2이하이면 +
def solution(s):
    s_arr = list(map(int, s))
    answer = s_arr[0]

    for i in s_arr[1:]:
        if answer == 0 or i < 2:
            answer += i
        else:
            answer *= i
    return answer

an = solution('02984')
print(an)

