#function Scope


a = 90 #here a is Global variable

def my_function():
    print(a)

my_function()

#---------------------------------------------------------------------------------------------------------

#Function inside Function : main function has it's own inner function (can have unlimited inner functions)

def main_function():
     var = 100

     def inner_function():
         print(var)

     inner_function()

main_function()


#---------------------------------------------------------------------------------------------------------

#LIST

count = [1,2,3,4]

def count_num(count):
    count.append(5)
    count[2] = 10
    return count

total = count_num(count)
print(total)



#we can write the above function as:

count = [1,2,3,4]

def count_num(bhumika):
    bhumika.append(6)
    return bhumika

total = count_num(count)
print(total)







