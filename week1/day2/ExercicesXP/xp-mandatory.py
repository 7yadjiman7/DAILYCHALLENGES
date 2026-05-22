# Exercice 1

# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

zip = zip(keys, values) # combined of two list

print(dict(zip)) # transform to the dictionary and print

# Exercice 2

"""
Loop through the family dictionary to calculate the total cost.
Print the ticket price for each family member.
Print the total cost at the end."""

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
sum = 0

for name, price in family.items():
    print(name,"ticket price is $", price)
    sum += price
print(sum)

# BONUS
"""
Allow the user to input family members’ names and ages, then calculate the total ticket cost."""

names = []
prices = []
while True:
    name = input("enter the name of one member of your family: ")
    if name == "quit":
        break
    age = int(input("enter the age of one member of your family: "))
    if age == 0:
        break
    elif age in [3,4,5,6,7,8,9,10,11,12]:
        price = 10
    elif age > 12:
        price = 15
    else: 
        price = 0
    names.append(name)
    prices.append(price)

zips = zip(names, prices)
sum = 0
for name, price in zips:
    print(name,"ticket price is ", price)
    sum += price
print(sum) 

# Exercice 3
# Create and manipulate a dictionary that contains information about the Zara brand.

brand = {"name": "Zara",
         "creation_date": 1975,
         "creator_name": "Amancio Ortega Gaona",
         "type_of_clothes": ["men", "women", "children", "home"],
         "international_competitors": ["Gap", "H&M", "Benetton"],
         "number_stores": 7000,
         "major_color":{
            "France": "blue", 
            "Spain": "red",  
            "US": ("pink", "green")
         }}

brand["number_stores"] = 2 #Change the value of number_stores to 2.

print(f"Zara's client are {brand["type_of_clothes"][0]}, or {brand["type_of_clothes"][1]}, or {brand["type_of_clothes"][2]}, or {brand["type_of_clothes"][3]}") #Print a sentence describing Zara’s clients using the type_of_clothes key.

brand["country_creation "] = "Spain" #Add a new key country_creation with the value Spain.

print(brand["international_competitors"]) #Check if international_competitors exists

brand["international_competitors"].append("Desigual")  # add “Desigual” to the list.

del brand["creation_date"] #Delete the creation_date key.

print(brand["international_competitors"][-1]) #Print the last item in international_competitors.

print(brand["major_color"]["US"]) #Print the major colors in the US

print(len(brand.keys())) #Print the number of keys in the dictionary.

print(brand.keys()) #Print all keys of the dictionary.

# BONUS
#Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {"creation_date": 1975,
                "number_stores": 7000}

merge = brand | more_on_zara
print(merge)

# Exercice 4
# Goal: Create a function that describes a city and its country.
def describe_city(city, country="Unknown"): #Define a Function with Parameters
    print(city," is in", country) #Print a Message

#Call the Function with different values
describe_city("Bouaké", "CI") 
describe_city("Paris")
describe_city("Madrid","Spain")

# Exercice 5
# Goal: Create a function that generates random numbers and compares them.
import random #Import the random Module

def randomFunction(number): #Define a Function with a Parameter
    number_generate = random.randint(1, 100) #Generate a Random Number
    if number == number_generate: # Compare the Numbers
        print("Good, it's the same value:")
    else:
        print("Oups, it is not the same!")
        print("enter value: ", number)
        print("Générate value: ", number_generate)

randomFunction(50) #Call the Function

# Exercice 6
# Goal: Create a function to describe a shirt’s size and message, with default values.
def make_shirt(size="large", text="I love python"): #Define a Function with Parameters
    print("The size of the shirt is", size, "and the text is", text) #Print a Summary Message

make_shirt() #Call make_shirt() to make a large shirt with the default message.
make_shirt(size="medium") # Call make_shirt() to make a medium shirt with the default message.
make_shirt("small","Custom message.") #Call make_shirt() to make a shirt of any size with a different message.

# Exercice 7
# Goal: Generate a random temperature and provide advice based on the temperature range.

import random # Import the random Module
def get_random_temp(): # Create the get_random_temp() Function
    # Return a random float between -10.0 and 40.0 degrees Celsius.
    return round(random.uniform(-10, 40), 1)


def get_temperature_advice(temp):  # Advice based on the temperature range
    if temp < 0:
        return "Brrr, that’s freezing! Wear some extra layers today."
    elif temp <= 16:
        return "Quite chilly! Don’t forget your coat."
    elif temp <= 23:
        return "Nice weather."
    elif temp <= 32:
        return "A bit warm, stay hydrated."
    else:
        return "It’s really hot! Stay cool."


def main():  # Create the main() Function
    deg = get_random_temp()  # Store the temperature in a variable
    # Print a friendly message
    print(f"The temperature right now is {deg} degrees Celsius.")
    print(get_temperature_advice(deg))  # Print temperature-based advice


main()

# Exercice 8
# Goal: Ask the user for pizza toppings and calculate the final price.

def pizza_toppings():
    toppings = []  # List to store toppings

    while True:  # Loop until the user types quit
        topping = input("Enter a pizza topping (or 'quit' to finish): ")
        if topping.lower() == "quit":
            break
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")

    print("\nYour pizza toppings:")
    for topping in toppings:
        print(f"- {topping}")

    total_cost = 10 + len(toppings) * 2.50  # Base price plus topping cost
    print(f"Total cost: ${total_cost:.2f}")


pizza_toppings()
