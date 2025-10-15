# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

print()
print("--- Conditionals in Python ---")
# Boolean refresher:
print( 3 == 2 )
print("Hello" == "Hi there")
print( 7 != 4)
print(4 > 5)

# if
num = 10
if num == 10:
    print("your number equals 10")
num1 = 13
if num1 <= 12:
    print("Your number is less then or equal to 12")
else:
    print("Your number is greater than 12")
#if elif else

temperature = 72
if temperature > 80: 
    print("It's hot!")
elif temperature >= 60:
    print("It's nice.")
else:
    print("It's cold!")

x = 16
y  = 13
if x == y:
    print("x is equal to y")
elif x < y:
    print("X is less than y")
elif x > y:
    print("X is greater than y")
else:
    print("Error")

# Logical operator: and
# Both sides of the 'and' must  be true, otherwise it's false. 


age = 16
has_permission = True

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("Can't drive yet")
    # Using 'or' and 'not'
print("--- Using 'or' --- ")
day = "Wednesday"

if day == "Saturday" or  day == "Sunday":
    print("It's the weekend!")
else:
    print("Its a weekday")

if day is not "Monday":
    print("It's not Monday")
import math
Num2 = int(input("Pick a even or odd number: "))
if Num2 %2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

Password = "gfbfhiperuvian"
Enter = input("Enter your password: ")
if Password is Enter:
    print("Access granted")
else:
    print("Access denied")

grade = int(input("Enter your grade: "))
if grade >= 90:
    print("You have an A")
elif grade >= 80:
    print("You have an B")
elif grade>= 70:
    print("You have a C")
elif grade >= 60:
    print("you have a 60")
else:
    print("you are failing")