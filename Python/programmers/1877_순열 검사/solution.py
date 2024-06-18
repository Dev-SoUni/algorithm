def solution(arr):
    arr.sort()

    for i in range(len(arr)):
        if i + 1 != arr[i]:
            return False

    return True