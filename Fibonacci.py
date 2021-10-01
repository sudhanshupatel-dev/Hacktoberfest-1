



nterms = int(input("How many terms? "))
n1 = 0
n2 = 1
count = 0
print("Fibonacci sequence:")
while count < nterms:
    print(n1,end=" ")
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1
