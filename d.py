mylist = list(map(int, input().split()))

for i in range(1, len(mylist)):
    if mylist[i] > mylist[i - 1]:
        print(mylist[i], end=' ')
