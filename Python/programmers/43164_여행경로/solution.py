def solution(tickets):
    answer = []
    path = dict()

    for idx, ticket in enumerate(tickets):
        start, end = ticket
        if start not in path:
            path[start] = []
        if end not in path:
            path[end] = []
        path[start].append((idx, end))

    def dfs(check_list, route):
        if check_list.count(0) < 1:
            answer.append(route.copy())
            return

        for i, destination in path[route[-1]]:
            if check_list[i] == 0:
                check_list[i] = 1
                route.append(destination)
                dfs(check_list, route)
                check_list[i] = 0
                route.pop()

    dfs([0] * len(tickets), ["ICN"])

    answer.sort()
    return answer[0]

s1 = solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
print(s1)
s2 = solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
print(s2)
