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

#Find and replace text
sentence = "I am you."
new_sentence = sentence.replace("Im",  "Youre")
other_replacement = sentence.replace("am", "are")
last_replacement = sentence.replace("you.", "me.")
print(sentence)
print(other_replacement)

#FORMATTED STRINGS

name = "Ada"
age = 28
city = "London"
print(f"Hello my name is {name}. I am {age} years  old and live in {city}")

print(f"Next year, ill be {age+1}")

Favorite_quote = input("Enter your favorite quote.")
length = (Favorite_quote)
sentence = ("Your quote is " + Favorite_quote + " and it is " + str(len(length)) + " letters long")
print(sentence)

First = input("First name:")
last = input("Last name:")
Info = last + ", " + First
print(Info)

word = "Yotei"
print(word.upper())
print(word [::-1])
print(word.lower())