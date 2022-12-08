# we start by writing our first code as usual ^^
print("Hello World!")

# we draw a triangle
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# using variable for the first time
character_name = "George"
character_age = "70"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age +"years old. ")
# we can change variables half the story by assigning a new value
character_name = "Mike"
print("He really liked the name " + character_name +", ")
print("but didn't like being " + character_age +".")


# in this way we can combine an int value with a str value and use them together : str()
character_age = 70
print("he was " + str(character_age) +" years old. ")

# boolean values must be capitalized True,False

print("Giraffe\nAcademy") # new line
print("Giraffe\"Academy") # escape
print("Giraffe\\Academy")

# concatenation
pharese = "Giraffe Academy"
print(pharese + " is cool")

# function we can use with string
print(pharese.lower())
print(pharese.upper())
print(pharese.islower()) # it turns True if it is all lower
print(pharese.lower().islower()) # we can use 2 function together
print(len(pharese)) # how many character
print(pharese[0]) # it gives us G 
print(pharese.index("G")) # it turns 0 
print(pharese.index("Acad")) # it gaves us where this line starts 7
print(pharese.index("z")) # error
print(pharese.replace("Giraffe","Elephant")) # Elephant Academy


# workind with numbers

from math import * 

print(abs(-7)) # 7
print(pow(3,2)) # 3 ^ 2 = 9
print(max(3,2)) # 3
print(min(3,2)) # 2
print(round(3.7)) # 4
print(floor(3.7)) # round the number lower
print(ceil(3.2)) # round the number up
print(sqrt(36))

# getting input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

#basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2) # When an external value is entered, python directly detects it as a string, so we need to specify that these are numbers.
# If we enter an integer, we will get an error when entering a decimal number.
print(result)

# madlibs game
color = input("Enter a color: ")
plural_noun = input("En#ter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are" + color )
print(plural_noun+" are blue")
print("I love " + celebrity)

# list
friends = ["Kevin","Karen","Jim"]

print(friends[-1]) #Jim
print(friends[1:]) #Karen,Jim
print(friends[1:2]) #range
friends[1] = "Mike" #modify values
1.10