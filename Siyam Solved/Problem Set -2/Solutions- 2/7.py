def EvenCount ():
    L = []
    count =sum([1 for i in range(1, 9) if i % 2 == 0])
    return count

def OddCount ():
    L = []
    count =sum([1 for i in range(1, 9) if i % 2 != 0])
    return count

print("Total EVEN numbers are:", EvenCount())
print("Total ODD numbers are:", OddCount())
