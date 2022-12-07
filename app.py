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
38.18
