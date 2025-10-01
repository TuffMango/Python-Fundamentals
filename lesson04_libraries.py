# Python libraries are repoistories of code that you can use in your own files.

#Key concepts: libraries in Python

#------------------
# MATH LIBRARY
#------------------
# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math
print("\n--- Math Library ---\n")

print("Square root: ", math.sqrt(25))
print("Round up to an integer: ", math.ceil(4.2))
print("Round down to an integer: ", math.floor(4.8))
print("Power: ", math.pow(2, 5))
print("Pi: ", math.pi)

#RANDOM LIBRARY
#challenge
seed = 14256.8
step_one = seed / 321
step_2 = step_one % 30
step_3 = step_2**2 / 4
print("Random seed thing:", math.floor(step_3))

import random #makes random stuff 

#methods:
print("random integer: " , random.randint(1, 100))
print(random.random()) #random float
print(random.choice(["eggs", "cheese", "chicken"])) 
mylist=["nufersinou", "uferioapnu", "gaieneriu"]
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)



#challange
radius = 7
circle_area = math.pi* radius ** 2
print(math.floor(circle_area))

print(random.randint(1, 6))

