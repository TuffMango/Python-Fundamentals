#INPUTS IN PYTHON

name = input("enter your name: ")
print("Hello")

age = int(input("Enter your age: "))
print(type(age))
age_number = int(age)
print("Next year, you will be:", age_number + 1)
print(type(age_number))

# Example with float input
height = float(input("Enter your height in meters: "))
print("You are", height, "meters tall.")


#CHALLENGES
color = input("Favorite color:")
print(type(color))
print("Your current favorite color is", color)

number = int(input("Choose 1 number:"))
number2 = int(input("choose another number:"))
print(int(number + number2))

import math
diameter = int(input("Provide a diameter"))
radius = diameter / 2
area = math.pi * radius **2

print("The area is" , math.floor(area))

import random
Amount = int(input("How many sides should the die have"))
print(random.randint(1, Amount) )
