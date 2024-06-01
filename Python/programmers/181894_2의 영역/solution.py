def solution(arr):
    if 2 not in arr:
        return [-1]
    txt = "".join(str(arr))
    print(txt)
    # arr.find(2)
    # arr.rindex(2)

solution(["1", "2", "1", "4", "5", "2", "9"])
solution([1, 2, 1, 4, 5, 2, 9])