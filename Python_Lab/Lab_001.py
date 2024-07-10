# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59



num = int(input("Enter a number: " ))


if num>=90 and num <=100:
    print("A")

elif num>=80 and num <=89:
    print("B")

elif num>=70 and num <=79:
    print("C")

elif num>=60 and num <=69:
    print("D")

elif num>=0 and num <=59:
    print("F")

else:
    print("Invalid number")















