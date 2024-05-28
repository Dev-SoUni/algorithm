def solution(s):
    answer = []
    s_arr = s.split(" ")

    for t in s_arr:
        a = ""
        for i in range(len(t)):
            if i == 0:
                a += t[i].upper()
            else:
                a += t[i].lower()
        answer.append(a)


    return " ".join(answer)
