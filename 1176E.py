from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())

        u -= 1
        v -= 1

        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n

    queue = deque([0])
    color[0] = 0

    group0 = [0]
    group1 = []

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:

            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]

                if color[neighbor] == 0:
                    group0.append(neighbor)
                else:
                    group1.append(neighbor)

                queue.append(neighbor)

    if len(group0) <= len(group1):
        answer = group0
    else:
        answer = group1

    print(len(answer))
    print(*(vertex + 1 for vertex in answer))