fact = 1
i = 1
 
num = int(input("Enter a number: "))
while i <= num:
    fact = fact*i
    i = i + 1
print("The factorial of", num, "is", fact)
