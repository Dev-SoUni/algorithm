def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([land[i-1][idx] for idx in range(4) if idx != j])
    return max(land[-1])


an = solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
print(an)