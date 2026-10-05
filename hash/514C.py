import sys

input = sys.stdin.readline

MOD1 = 10 ** 9 + 7
MOD2 = 10 ** 9 + 9
BASE = 31


def value(c):
    return ord(c) - ord('a') + 1

n, m = map(int, input().split())

words = [input().strip() for _ in range(n)]
queries = [input().strip() for _ in range(m)]

max_len = 0

for s in words:
    max_len = max(max_len, len(s))

for s in queries:
    max_len = max(max_len, len(s))

powers1 = [1] * (max_len + 1)
powers2 = [1] * (max_len + 1)

for i in range(1, max_len + 1):
    powers1[i] = powers1[i - 1] * BASE % MOD1
    powers2[i] = powers2[i - 1] * BASE % MOD2

def get_hash(s):
    hash1 = 0
    hash2 = 0

    for i in range(len(s)):
        x = value(s[i])

        hash1 = (hash1 + x * powers1[i]) % MOD1
        hash2 = (hash2 + x * powers2[i]) % MOD2

    return hash1, hash2

hashes = set()

for s in words:
    hash1, hash2 = get_hash(s)

    hashes.add((len(s), hash1, hash2))

for s in queries:

    hash1, hash2 = get_hash(s)

    found = False

    for i in range(len(s)):
        old_value = value(s[i])

        for new_char in "abc":
            if new_char == s[i]:
                continue

            new_value = value(new_char)

            new_hash1 = (hash1 + (new_value - old_value) * powers1[i]) % MOD1
            new_hash2 = (hash2 + (new_value - old_value) * powers2[i]) % MOD2

            if (len(s), new_hash1, new_hash2) in hashes:
                found = True
                break

        if found:
            break

    if found:
        print("YES")
    else:
        print("NO")