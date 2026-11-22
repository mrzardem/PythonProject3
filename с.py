mylist = list(map(int, input().split()))

count = 0

for x in mylist:
    if x > 0:
        count += 1

print(count)
