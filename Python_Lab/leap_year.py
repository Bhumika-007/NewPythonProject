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


# ---------------------------------------------------------------------------------------------------------------------

    # leap year with function
    def leap_year(year):
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False


    year = int(input("Enter the year"))

    if leap_year(year):
        print("leap year")
    else:
        print("not")


