mylist = list(map(int, input().split()))

for i in range(len(mylist) - 1):
    if mylist[i] * mylist[i + 1] > 0:
        print(mylist[i], mylist[i + 1])
        break
