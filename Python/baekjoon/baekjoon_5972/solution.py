import heapq

N, M = map(int, input().split())
delivery = {}

for _ in range(0, M):
    a, b, c = map(int, input().split())
    if a not in delivery.keys():
        delivery[a] = {b: c}
    else:
        delivery[a].update({b: c})
    if b not in delivery.keys():
        delivery[b] = {a: c}
    else:
        delivery[b].update({a: c})




print(N)
print(M)
print(delivery)