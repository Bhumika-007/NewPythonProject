# ARGS: any number of arguments

def print_argument(*arg):  # created own print_argument function
    for i in args:  # i variable IN arguments
        print(i, end="\n")


print("bhum", "nit", "ruch")


#--------------------------------------------------------------------------------


#*args --> List
a = ["abc", "efg", "hij"]
for i in a:
    print(i)


#--------------------------------------------------------------------------------

def make_pizza(*toping, base):
    print(toping, base)

bhumika = make_pizza("mushroms", "tomato", "brocolli", base= "thin crust")