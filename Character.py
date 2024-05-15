char=input("Enter a character:")
if char.isupper():
    char=char.lower()
elif char.islower():
    char=char.upper()
print(char)
