
a = list(map(int, input().split()))

k = 0

for i in range(len(a)):
    if a[i] != 0:
        a[k] = a[i]
        k += 1

for i in range(k, len(a)):
    a[i] = 0

print(*a)
