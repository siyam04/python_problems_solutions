def ReturnOdd():
    print("How Many Elements?")
    e = int(input())
    L = []
    print("Enter", e, "Elements:")
    for i in range(e):
        L.append(int(input()))
    return (L[1::2])

print("The Elements of Odd index are:", ReturnOdd())
