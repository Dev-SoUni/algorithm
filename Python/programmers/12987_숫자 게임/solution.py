def solution(A, B):
    A.sort()
    B.sort()
    l = len(A)
    b_start = 0
    check_list = [0] * l

    for a_val in A:
        for idx in range(b_start, l):
            if check_list[idx] == 0 and a_val < B[idx]:
                check_list[idx] = 1
                b_start = idx
                break

    return check_list.count(1)

def solution2(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

    return answer