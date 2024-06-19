answer = 0

def dfs(k, cnt, dungeons, check_list):
    global answer
    answer = max(cnt, answer)

    for i in range(len(dungeons)):
        if check_list[i] == 0 and dungeons[i][0] <= k:
            check_list[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons, check_list)
            check_list[i] = 0

def solution(k, dungeons):
    global answer
    dfs(k, 0, dungeons, [0] * len(dungeons))

    return answer

result = solution(80, [[80,20],[50,40],[30,10]])
print(result)