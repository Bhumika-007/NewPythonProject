# Develop a Python script that calculates the square and cube of a given number.

num = float(input("Enter the number \n"))

square = num ** 2
cube = num ** 3

print(f"The square of {num} is {square} and the cube is {cube}")




# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.


num1 = float(input("Enter the first number \n"))
num2 = float(input("Enter the second number \n"))


if num1 > num2:
    print("num1 is greater than num2")

elif num1 < num2:
    print("num2 is greater than num1")

else:
     print("num1 is equal to num2")