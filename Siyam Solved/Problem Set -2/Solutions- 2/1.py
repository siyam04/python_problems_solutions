def AddList():
    print("How Many Values?")
    v = int(input())

    L = []

    for i in range(v):
        print("Enter", i, "No. Value:")
        L.append(int(input()))

    return L, sum(L)

print("List and Addition of List is:", AddList())
