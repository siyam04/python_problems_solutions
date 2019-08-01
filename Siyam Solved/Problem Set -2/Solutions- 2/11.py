start = int(input('Enter Starting Year: '))
end = int(input('Enter Starting Year: '))

print("Leap Years Between", start, "and", end, "is:")

while (start <= end):
    if (start % 4 == 0 and start % 100 != 0):
       print(start)
    if (start % 100 == 0 and start % 400 == 0):
       print (start)
    start = start + 1
