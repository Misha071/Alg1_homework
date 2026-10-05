count = {}

n = int(input())

for _ in range(n):
    name = input()

    if name not in count:
        print("OK")
        count[name] = 0
    else:
        count[name] += 1
        print(f"{name}{count[name]}")