
a = list(map(int, input().split()))
k = int(input())

k %= len(a)

a.reverse()
a[:k] = reversed(a[:k])
a[k:] = reversed(a[k:])

print(*a)
