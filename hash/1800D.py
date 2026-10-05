import sys

input = sys.stdin.readline

MOD1 = 10 ** 9 + 7
MOD2 = 10 ** 9 + 9
BASE = 31

def value(c):
    return ord(c) - ord('a') + 1

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    m = n - 2

    power1 = [1] * (m + 1)
    power2 = [1] * (m + 1)

    for i in range(1, m + 1):
        power1[i] = power1[i - 1] * BASE % MOD1
        power2[i] = power2[i - 1] * BASE % MOD2

    hash1 = 0
    hash2 = 0

    for c in s[2:]:
        x = value(c)

        hash1 = (hash1 * BASE + x) % MOD1
        hash2 = (hash2 * BASE + x) % MOD2

    seen = set()

    for i in range(n - 1):
        seen.add((hash1, hash2))

        if i == n - 2:
            break

        old_char = value(s[i + 2])
        new_char = value(s[i])

        degree = m - 1 - i

        hash1 = (hash1 + (new_char - old_char) * power1[degree]) % MOD1
        hash2 = (hash2 + (new_char - old_char) * power2[degree]) % MOD2

    print(len(seen))