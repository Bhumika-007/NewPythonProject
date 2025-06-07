#WAP to take user age and check whether he can go the club

age = int(input("Enter your age: \n"))

if age > 18:
    print("The user can go the club")

elif age < 18:
    print("The user do not go to the club")

elif age == 18:
    print("The user can go to the club")

else:
    print("No One")

