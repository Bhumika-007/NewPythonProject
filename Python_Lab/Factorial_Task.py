n = int(input("Enter the number: \n"))
fact = 1
for i in range(1,n+1):
    fact = fact * i
    print("\nThe factorial of number is:", fact)