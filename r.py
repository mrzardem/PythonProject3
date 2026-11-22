
a = list(map(int, input().split()))
k, c = map(int, input().split())

a.append(0)

for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]

a[k] = c

print(*a)
