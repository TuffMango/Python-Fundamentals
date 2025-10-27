# LOOPS IN PYTHON
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.
# The for-loop.
# A for-loop repeats for each element in a sequence (like a list or string).

animals = ["lamb", "sheep", "cow", "goose", "donkey" ]
print("These are the animals: ", animals )
import time
for x in animals: 
    print("Now petting a", x)
    time.sleep(1.5)
    if animals == "sheep":
        print("Hi sheep!")
print("\nNow I have pet all the animals")

for i in range(2, 11, 2):
    print("Counting: ", i)


for num in range(2, 11, 2):
    print("Even Number: ", num)

#STRINGS
fav_word = "Shenangians"
letter_list = []

for letter in fav_word:
    print(letter, end=" ")
    letter_list.append(letter)

print(letter_list)

#WHILE LOOPS

count = 0

while count < 5:
    print(f"Loopin. On loop number {count}.")
    count += 1
    time.sleep(.5)

    print("we out of the loop")

user = "stop"
while user != "exit":
    user = input("type stop to escape")   

count = 60
increment = 1

while count > 0:
    count -= increment
    increment += 1
        
    if count < 0:
        break

    print(count)


