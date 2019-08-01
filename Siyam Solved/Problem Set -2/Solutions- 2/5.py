def FtoC(f):
    c = round((f - 32) * 5 / 9)
    return c

def CtoF(c):
    f = round((c * 9 / 5) + 32)
    return f

print("Enter Celsius:")
c = int(input())
print(c,"°C is",CtoF(c),"in Fahrenheit" )

print("\nEnter Fahrenheit:")
f = int(input())
print(f,"°F is",FtoC(f),"in Celsius" )

