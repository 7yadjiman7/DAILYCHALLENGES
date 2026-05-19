# Exercice 1

# Print the following output using one line of code:

# Hello world
# Hello world
# Hello world
# Hello world

print("Hello world\n" * 4)

# Exercice 2

# Write code that calculates the result of:

# (99^3)*8 (meaning 99 to the power of 3, times 8).

result = (99 ** 3) * 8
print(result)

# Exercice 3

# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare

# Example:

# >>> 15 < 8 #False
# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"

5 < 3 #False
3 == 3 #True
3 == "3" #False
#"3" > 3 Error
"Hello" == "hello" #False

# Exercice 4
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = "HP"
print(f"I have a {computer_brand} computer.")

#exercice 5
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = "Couibaly"
age = 24    
shoe_size = 43
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}."
print(info)

# Exercice 6
# Instructions
# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World"

a = 10
b = 5   
if a > b:
    print("Hello World")

# Exercice 7
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.

number = int(input("Please enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")   
else:
    print(f"{number} is an odd number.")

# Exercice 8
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

name = input("Please enter your name: ")
if name == "Coulibaly":  
    print("Wow, we have the same name!")
else:    
    print("Oh, we have different names!")

# Exercie 9
# Instructions
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

height = int(input("Please enter your height in centimeters: "))
if height > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")