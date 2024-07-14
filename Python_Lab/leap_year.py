#A leap year is divisible by 4, but not by 100 unless it is also divisible by 400. Use an if-else statement to make this determination.

year = int(input("Enter the year: \n"))

if year % 4 == 0:
    print("the year is leap year")

elif year % 100 != 0:
    print("The year is not a leap year")

elif year % 400 == 0:
    print("The year is also a leap year")

else:
    print("No idea")


