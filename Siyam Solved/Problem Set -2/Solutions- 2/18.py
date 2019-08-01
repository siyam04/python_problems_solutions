L = ["Hello", "World", "in", "a", "frame"]

for i in range(1, 10):
    print('*', end='')

print()

for j in L:
    print("*", j, end=' ')
    n = len(j)
    if(n < 5):
        for m in range(0, 5 - n):
            print(" ", end='')
    print("*")

for k in range(1, 10):
    print('*', end='')

