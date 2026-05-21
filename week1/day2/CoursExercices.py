# exercice 1
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict["class"]["student"]["marks"]["history"])

#Exercice 2

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
print(sample_dict)

for key in keys_to_remove:
    sample_dict.pop(key, None)

print(sample_dict)

# Exemple of use "zip" in for loop

list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3): # only go as far it is possible
    print(item)

# Exemple of "end" usage

for letter in 'Leonardo':
    if letter == 'a':
        break
    print(letter, end='') # end='' renders each letter next to the other


# Exemple usage of break

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')

# Exemple usage of continue

for letter in 'Leonardo':
    if letter == 'o':
        continue
    print(letter, end='') # dont execute for 'o' letter


# Exemple usage pass

for item in [1,2,3]:
    # comment
    pass # to avoid the error

print('Finish the script')


#Exercice 3

values = []
while True:
    dictionary_values = input("Enter your dictionary values: ")
    if dictionary_values.lower() == "quit":
        break
    values.append(dictionary_values)

dictionary = dict(enumerate(values))

print(dictionary)

# Exercice

def calculation(a, b):
    addition = a + b
    soustraction = a - b

    return addition, soustraction

result = calculation(10, 20)
print(result)

# Exercice

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

def reduce(elt):
    newList = []
    if len(elt) <= 4:
        newList.append(elt)
    return newList
            
print(list(map(lambda n: print("Hello ", n), filter(reduce, people))))
