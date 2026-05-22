# Exercice 1: Cars

compagnies =["Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet"]
print(" how many manufacturers/companies are in the list? ")
print(sorted(compagnies, reverse=True))

letter_o =[]
letter_i =[]
count_o = 0
count_i = 1
for i in compagnies:
    if "o" in i:
        letter_o.append(i)
        count_o += 1
    elif "i" not in i:
        letter_i.append(i)
        count_i += 1
print("The number of manufacturers’ names have the letter o in them is ", count_o)
print("The number of manufacturers’ names do not have the letter i in them is ", count_i)