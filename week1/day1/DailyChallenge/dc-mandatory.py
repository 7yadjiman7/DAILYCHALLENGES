#Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples
# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

number = int(input("Please enter a number: "))
length = int(input("Please enter a length: "))  
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# user's word : "ppoeemm" ➞ "poem"


user_string = input("Please enter a string: ")
result_string = ""
for i in range(len(user_string)):
    if i == 0 or user_string[i] != user_string[i - 1]:
        result_string += user_string[i]
print(result_string)





