n1, n2 = 0, 1
count = 0

print("Fibonacci sequence upto 10th term:",n1,n2,end=" ")
while (count < 8):
    next_term = n1 + n2
    print(next_term,end=" ")
    n1 = n2
    n2 = next_term
    count += 1