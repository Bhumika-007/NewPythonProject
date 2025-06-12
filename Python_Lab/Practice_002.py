#FUNCTIONS: block of code which can be executed or reused.
#definition
#calling

def greet():
    print("bhumika")
greet()  #No return type function with No Arguments / parameters

#--------------------------------------------------------------------------------


def Name(name):   #name in bracket is called as Argument.
    print("Hi, how are you", name)

Name("Bhumika")
Name("Nitish")
Name(123)
Name("234") # No return type but with Arguments / parameters


#--------------------------------------------------------------------------------

def allowed_to_enter_club(age,card):
    if age == 18:
        if card == "present":
            print("You are allowed")
        else:
            print("Not allowed")

allowed_to_enter_club(18, "Not present") #return type function with Argumets / parameters

#--------------------------------------------------------------------------------


#no return type with default argument
def allowed_with_name(name="Bhumika"): #default value in argument
    print("hello", name)

allowed_with_name()
allowed_with_name("nitish")
allowed_with_name(name="ruchika")




#--------------------------------------------------------------------------------

#arguments with return type
def addition_of_values(a, b):
    return a + b

result = addition_of_values(3, 4)
result = addition_of_values(a=20, b=30)
result = addition_of_values(b=25, a=30)

print(result)

#OR

print(addition_of_values(b=25, a=30))


#--------------------------------------------------------------------------------





