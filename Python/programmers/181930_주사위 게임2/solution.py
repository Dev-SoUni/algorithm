def solution1(a, b, c):
    answer = a + b +c
    if (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
        answer *= (a**2 + b**2 + c**2)
    if a == b and a == c and b == c:
        answer *= (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)

    return answer

def solution2(a, b, c):
    check = len(set([a, b, c]))
    if check == 1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check == 2:
        return (a+b+c) * (a**2+b**2+c**2)
    else:
        return (a+b+c)