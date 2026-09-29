n = int(input())
f = list(map(int, input().split()))

for i in range(n):
    f[i] -= 1

for i in range(n):
    if f[f[f[i]]] == i:
        print("YES")
        break

else:
    print("NO")