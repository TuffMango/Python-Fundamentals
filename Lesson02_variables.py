#Concept variables
#stored in physical storage of computer and holds a value
taco = "hello world"
password = "Matater"
email = "idkimnotputtingmyemail@gmail.com"
print("password:\t", password)
print("email:\t", email)

temperature = 96.7
print(type (temperature))
price = 3.99

enable = False
is_complete = True
print(is_complete)
print(enable)
#can overwrite variables
enable = True
print(enable)
#variable name must be meaningful, dont use algebraic for variables unless it's math
x = 3.14
y = 2
print(x + y)
print(x+y != 5.14)
print(x+y == 5.140000000000001)
# Variables are flexible. You create or update another variable like so
count = 10
count_down = count - 1
print(count)
print(count_down)
count = count_down
print(count)
count_down = count - 1
print(count_down)
count = count_down
print(count)



#challange 1:rename variables to match
name = "Radia Pearlman"
age = 34
profession = "Networking Engineer"

#create a variable called count wiht a value oof 10, inrease it by 5 and print result
count = 10
count_5 = count + 5
print(count)
print(count_5)

#challange 3: swap values of 2 variables
x2 = 4
y2 = "hello"
temp = y2
y2 = x2
x2 = temp
print(x2)
print(y2)


#challange 4: boolean
is_raining = False
is_raining = True
print("is it raining?", is_raining)