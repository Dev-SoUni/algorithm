def solution(n):
    n_arr = [0 for _ in range(n+1)]
    n_arr[1] = 1
    if n > 1:
        n_arr[2] = 2

    for i in range(3, n+1):
        n_arr[i] = n_arr[i-2] + n_arr[i-1]

    return n_arr[n]%1234567
