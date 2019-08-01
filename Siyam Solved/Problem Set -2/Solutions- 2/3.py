def CountList(L):
    count=0

    for i in L:
        if len(i)>=2 and i[0] == i[-1]:
            count= count+1

    return count

print("Count is:", CountList(['abc', 'xyz', 'aba', '1221']))



