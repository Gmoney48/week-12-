# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)  # Checks for equality # False
print(a != b)  # Checks if is not equal # True
print(a > b)   # Checks for greater than # False
print(a < b)   # Checks fpr ;ess than # True
print(a >= b)  # Checks for greater than or equal to # False
print(a <= b)  # Checks for less than or equal to # True


#predict the output of the following comparisons:
10 > 5 #True
7 == 2 * 3 + 1 #True
8 != 8 #True
4 <= 2 + 2 #True

# Write 3 examples that result in True and 3 that result in False.
print(a + 1 == b) #True
print(a <= b) #True
print(a - 1 == b - 2) #True
print(a * 3 <= b) #False
print(a + b == 3) #False
print(a * b <= a + b) #False
# Create a simple grade-checking condition:
# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
#Asking student for score
score = int(input("What is your score?"))
# make this program for all grading spectrums
# if the score is between 90-100 .. you got an A 
# if the score is between 80-89 .. you got a B
# if the score is between 70-79 .. you got a C
# if the score is between 60-69 .. you got a D
# else you failed
if score >= 60:
    print("you passed the test")
else: 
    print("you didn't pass")
#Ask for a password
password = input("What is your password?")
score = int(input("What is your score"))
if score >= 90:
    print("You got an A")
elif score >= 80 and score <= 89:
    print("You got a B")
elif score >= 70 and score <= 79:
    print("You got a C")
elif score >= 60 and score <= 69:
    print("You got a D")
else:
    print("You failed")