print("Enter an Integer:")

n = int(input())

if(n < 0):
    print("Negative input. Please Enter positive Integer: ")
else:
    for i in range(0, n):
        print(i ** 2)