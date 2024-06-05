def solution(arr):
    # 총 그룹의 수
    answer = 0
    # 현재 그룹에 포함된 모험가의 수
    count = 0
    arr.sort()

    for i in arr:
        # 현재 그룹에 해당하는 모험가 추가
        count += 1
        # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 생성
        if count >= i:
            answer += 1
            count = 0

    return answer


solution([2, 3, 1, 2, 2])
