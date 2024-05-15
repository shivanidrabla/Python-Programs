number = int(input ("Enter the number: "))  
range_limit=int(input("Enter the range:"))       
print ("The Multiplication Table of:", number)  
for i in range(1, range_limit+1):      
   print (number, 'x', i, '=', number * i)    