n = int(input())

tree = [[] for _ in range(n)]
roots = []

for employee in range(n):
    manager = int(input())

    if manager == -1:
        roots.append(employee)
    else:
        tree[manager - 1].append(employee)

answer = 0

def dfs(node, depth):
    global answer

    answer = max(answer, depth)

    for child in tree[node]:
        dfs(child, depth + 1)

for root in roots:
    dfs(root, 1)

print(answer)