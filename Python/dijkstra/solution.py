import heapq

my_graph = {
    "A": {
        "B": 8,
        "C": 1,
        "D": 2
    },
    "B": {},
    "C": {
        "B": 5,
        "D": 2
    },
    "D": {
        "E": 3,
        "F": 5
    },
    "E": {
        "F": 1
    },
    "F": {
        "A": 5
    }
}


def dijkstra(graph, start):
    distances = {}
    for key in graph:
        distances[key] = float('inf')
    distances[start] = 0

    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        item = heapq.heappop(queue)
        current_distance = item[0]
        current_node = item[1]

        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    print(distances)


dijkstra(my_graph, "A")

