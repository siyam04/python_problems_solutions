print("How Many Numbers?")
n = int(input())

L = []

for i in range(n):
    print("Enter", i, "No. Value:")
    L.append(int(input()))

print("List is:", L)
L.sort()
print("Smallest number is:", L[0])
