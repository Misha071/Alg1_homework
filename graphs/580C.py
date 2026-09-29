n, m = map(int, input().split())
cats = list(map(int, input().split()))

tree = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    tree[a].append(b)
    tree[b].append(a)

answer = 0

def dfs(node, parent, cats_in_row):
    global answer

    if cats[node] == 1:
        cats_in_row += 1
    else:
        cats_in_row = 0

    if cats_in_row > m:
        return

    is_leaf = True

    for child in tree[node]:
        if child == parent:
            continue

        is_leaf = False

        dfs(child, node, cats_in_row)

    if is_leaf:
        answer += 1

dfs(0, -1, 0)
print(answer)