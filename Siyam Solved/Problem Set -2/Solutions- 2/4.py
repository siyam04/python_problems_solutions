def CheckList(L):
    if (not L):
        return  False
    else:
        return True

print("Enter a value or Leave Empty:")
n = []

for i in input():
    n.append(input())

print("List is:", CheckList(n))


