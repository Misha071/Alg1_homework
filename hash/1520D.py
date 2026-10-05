t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = {}
    ans = 0

    for i in range(n):
        x = a[i] - i

        if x in count:
            ans += count[x]
            count[x] += 1
        else:
            count[x] = 1

    print(ans)