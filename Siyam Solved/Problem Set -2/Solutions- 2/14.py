def CheckPalindrome(string):
    if (string == string[::-1]):
        return True
    else:
        return False

s = input("Enter a String:\n")
print(CheckPalindrome(s))
