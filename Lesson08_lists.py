#LISTS
#ists mutiple values in one variable
#They are ordered, changable, and allow duplicates

#initialize a list with brackets:
empty_list = []

animals = ["donkey", "pangolin", "blobfish"]
numbers = [2, 4, 6, 8, 10]
mixed = ["piffle", 42, True, 9.99]

print(animals)
print(numbers)
print(mixed)

print()
print()
print()
print("--- Indexing: how to access the elements of a list ---")
print("First Element:", animals[0])
print("Second element:", animals[1])
print("Last element:", animals[-1])

animal_to_replace = animals.index("blobfish")
print(animal_to_replace)
animals[animal_to_replace] = "seamonkey"

print()
print("--- Modifying Lists ---")
animals[0] = "babirusa"
print(animals)

#Add elements
animals.append("Glass frog")
print(animals)

# insert element at specific index
animals.insert(3, "aye-aye")
print(animals)
animals.insert(1, "camel")
print("Inserted another animal:", animals)

#removing
animals.remove("pangolin")
print(animals)

last_animal = animals.pop()
print(last_animal)
print("remaining: ", animals)

nums = [3, 7, 8, 2, 1, 6, 9]
print("original numbers: ", nums)

print("Length of lists ", len(nums))
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))

nums.sort()
print(nums)
if "cat" in animals:
    print("Cat is in the list!")
else:
    print("Cat is not in the list.")

#copying lists
new_list =[1, 2, 3]
copied_list= new_list.copy()
copied_list.append(4)
print(new_list)
print(copied_list)

#Nested lists

matrix = [  
    [1,2,3], 
    [4,5,6], 
    [7,8,9]  
    ] 

print(matrix[2])
print(matrix[0][2])
print(matrix[2][2])


#challenges
num_list = [1, 2, 3, 4, 5, 6]
new_int = int(input("Please enter a number: "))
num_list.insert(2, new_int)
print(num_list)

shopping = []
shopping.append["cookie", "Eggs"]
shopping.remove["eggs"]
print(shopping)

