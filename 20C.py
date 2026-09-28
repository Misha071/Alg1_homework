import heapq


def dijkstra(graph, start):
    distance = {}
    parent = {}

    for node in graph:
        distance[node] = float("inf")
        parent[node] = -1

    distance[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, node = heapq.heappop(heap)

        if current_distance > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance

                parent[neighbor] = node

                heapq.heappush(heap, (new_distance, neighbor))

    return distance, parent


n, m = map(int, input().split())

graph = {}

for node in range(1, n + 1):
    graph[node] = []


for _ in range(m):
    u, v, weight = map(int, input().split())

    graph[u].append((v, weight))
    graph[v].append((u, weight))


distance, parent = dijkstra(graph, 1)


if distance[n] == float("inf"):
    print(-1)

else:
    path = []

    current = n

    while current != -1:
        path.append(current)

        if current == 1:
            break

        current = parent[current]

    path.reverse()

    print(*path)