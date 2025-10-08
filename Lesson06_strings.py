#Basic string creation and indexes
greeting = "hello"
name = "Ada"
print(greeting, name)

messege = greeting +" " + name + "!!!"
print("Concatecated message:", messege)

print(greeting[4])

word = "Supercalifragilisticexplialidocious"
print(word[0])
print(word[::-1])
print(word[-1])
print(word[5:9])

##BUILT IN FUNCTIONS

country = "Jamacia"
length_of_word = len(country)
print(length_of_word)

phrase = "spOngEbOb"
print("uppercase:", phrase.upper())
#opposite for lowercase
print("Capitilized:", phrase.capitalize())