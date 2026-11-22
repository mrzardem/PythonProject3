
a = list(map(int, input().split()))

mx = 0
num = a[0]

for i in a:
    if a.count(i) > mx:
        mx = a.count(i)
        num = i

print(num)
