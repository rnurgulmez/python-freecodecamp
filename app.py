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

# list (mutable)
friends = ["Kevin","Karen","Jim"]

print(friends[-1]) #Jim
print(friends[1:]) #Karen,Jim
print(friends[1:2]) #range
friends[1] = "Mike" #modify values

# list function
lucky_number = [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Tim"]
friends.extend(lucky_number) # add lists together
friends.append("Creed") # add the item at end of the list
friends.insert(1,"Kelly") # we can add the item wherever we want
friends.remove("Jim") 
friends.clear() # reset list
friends.pop() # pop off of the list,removes the last element
print(friends.index("Kevin")) # gaves us index of Kevin
print(friends.count("Jim")) # how many jim do we have?
friends.sort() # asc order
lucky_number.reverse() # reverse the order
friends2 = friends.copy() 

# tuples :  a collection of objects separated by commas(immutable)
coordinates = (4,5) # we can't add,delete,modify,change () tuple [] list
print(coordinates[0])

# function
def say_hi():
    print("Hello User") # any code inside the function needs to be indented
 
say_hi()
....
def say_hi(name):
    print("Hello "+name)

print("Top")
say_hi("Rabia")
print("Bottom")

# return 
def cube(num) :
    return num*num*num # after return we can't put anything because it breaks the function here

result = cube(4)
print(result)

# if statements
is_male = False

if is_male:
    print("You are a male")  # indentation
else:
    print("You are a female")
    
....
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You either not male or not tall or both")
  
# comparison
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return  num2
    else:
        return num3

print(max_num(3,4,3))

# better calculator
num1 = float(input("Enter first number : ")) # Whatever the user enters, it is perceived as a string, but we want to convert it to a number here immediately.
op = input("Enter operator : ")
num2 = float(input("Enter second number : "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator")
    
# dictionaries : We use dictionaries to store key/value pairs.
monthConversions = {
    #we want to convert 3 digits month name into the full name
    "Jan" : "January", # "key" : "value"
    "Feb" : "February",  # every key needs to be unique
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
}

print(monthConversions["Apr"])
print(monthConversions.get("Apr")) # 
print(monthConversions.get("Luv","Not a valid key"))

# while loop
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")

# building a guessing game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and  not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess : ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE")
else:
    print("You win!")

# for loop
for letter in "Giraffe Academy":
    print(letter)   # it will print out every single charachter
 ....   
friends = ["Karen","Jim","Kevin"]

for friend in friends:
    print(friend)
    
...

for index in range(10):   or range(3,10)  # Increases numbers from 3 to 10, not including 10
    print(index)
    
....
friends = ["Karen","Jim","Kevin"]

for index in range(len(friends)):   # karen,jim,kevin 
    print(friends[index])
    
....

friends = ["Karen","Jim","Kevin"]

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")
        
# exponent function

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))

# 2D Lists and Nested Loops

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0]) # 1

for row in number_grid:  # returns values in each column
    for column in row:
        print(column)
        
        
# Build a translator
# any vowels becomes 'g'


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase : ")))

# Comment

# 

'''
also comment
'''

# Try / Except 

try:
    number = int(input("Enter a number : "))
    print(number)
except:
    print("Invalid value")

# catching spesific errros

try:
    value = 10 / 0
    number = int(input("Enter a number : "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid value")
    
# Reading files
# r= read, w=write, a=append, r+= read+write

employee_file = open("employees.txt", "r")

print(employee_file.read()) # we can check by readable() if it can be read or not
print(employee_file.readline())  # it can read only the first line
print(employee_file.readline())  # now the second one
print(employee_file.readlines()) # take all of the lines and put them in a list
print(employee_file.readlines()[1]) # gives us the second item of this list

employee_file.close()   # whenever we open a file,we need to close it too


....


employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)
    
employee_file.close()

# Writing and Appending Files

employee_file = open("employees.txt", "a")

employee_file.write("\nomer")

employee_file.close()


...

# if you in a mode w it will override in that existing file

employee_file = open("employees1.txt", "w") # we create new file

employee_file.write("\nomer")

employee_file.close()

# modules
import useful_tools

print(useful_tools.roll_dice(5)) # we can use module from external py file

# there is a built-in function whereas external function
# all of the external modules stores in lib folder unlike built-in functions
# If we want to use an external module, we can google it and download it.
# pip is like python manager
