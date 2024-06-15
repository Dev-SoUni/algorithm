graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "G", "H", "I"],
    "D": ["B", "E", "F"],
    "G": ["C"],
    "H": ["C"],
    "I": ["C", "J"],
    "E": ["D"],
    "F": ["D"],
    "J": ["I"],
}

need_visit = ["A"]
visited = list()

while need_visit:
    item = need_visit.pop()
    if item not in visited:
        visited += item
        need_visit.extend(graph.get(item))
print(visited)
# print(need_visit)
