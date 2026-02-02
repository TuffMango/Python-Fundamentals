#Python functions are blocks of code that you can reuse
#to run a function you call the function by writining its name followed by parathensis and any argument that it needs

def say_hi():
    print("hi")

def say_bye():
    print("bye")


say_hi()
say_bye()

print("\nexample 2")

def express_this(e):
    return e
 #e is a parameter, a replacement for an argument
expression = (1 + 2)

print(expression)
expression2 = (45*2.19244184021-481-453259259102)
print(expression2)



print("ex. 3")

def greeter(n):
    return f"HI BOIIIIIIIIIIII {n}"


first = greeter("jojo")
second = greeter("bizbo")
third = greeter("dio")
print(first, second, third)

def remainder(a, b):
    return a % b

result = remainder(3,2)

print("remainder ", result)

def is_far(distance):

    if distance < 1:
        return "error"
    
    if distance >= 100:
        return "thats far"
    elif distance < 100 and distance > 20:
        return "i can get there fast"
    elif distance < 20:
        return "thats close"

    

print(is_far(-400))



def double_sequencer(number, times):
    value = number
    sequence = []
    for i in range(times):
        value = value * 2
        sequence.append(value)
    return sequence

result = double_sequencer(1, 5)
print(result)
