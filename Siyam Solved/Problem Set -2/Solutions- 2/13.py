def RunningList(L):
    n = len(L)
    SumList = []
    sum = 0
    for i in range(0, n):
        sum = sum + L[i]
        SumList.append(sum)
    return SumList

print("Enter any list: ")
t = [int(i) for i in input().split()]
result = RunningList(t)
print(result)
