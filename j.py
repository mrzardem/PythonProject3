
a = list(map(int, input().split()))
x = int(input())

n = 1

for i in a:
    if i >= x:
        n += 1

print(n)
