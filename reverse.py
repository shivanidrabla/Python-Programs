a=int(input("Enter a number:"))
rev=0
t=a
while(a>0):
        b=a%10
        rev=rev*10+b
        a=a//10
print("Reverse:",rev)
if(t==rev):
    print("Palindrome")
else:
    print("Not a palindrome")