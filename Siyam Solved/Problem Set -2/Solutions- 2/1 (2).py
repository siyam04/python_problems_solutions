print("How Many Values?")
v = int(input())

L = []

for i in range(v):
    print("Enter", i, "No. Value:")
    L.append(int(input()))

print("List is:", L)
print("Summation is:", sum(L))



