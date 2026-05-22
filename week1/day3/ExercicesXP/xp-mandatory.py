# Exercice 1: Cats
"""Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details."""
class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Step 1: Create cat objects
cat1 = Cat("dodo", 10)
cat2 = Cat("pheno", 20)
cat3 = Cat("pato", 30)

# Step 2: Create a Function to Find the Oldest Cat
# Fix: comparer chaque chat avec `oldest` directement (liste[i-1] causait un bug à i=0)
def comparaison(cat1, cat2, cat3):
    liste = [cat1, cat2, cat3]
    oldest = liste[0]
    for cat in liste:
        if cat.age > oldest.age:
            oldest = cat
    return oldest

# Step 3: Print the Oldest Cat's Details — Fix: format demandé
cat_oldest = comparaison(cat1, cat2, cat3)
print(f"The oldest cat is {cat_oldest.name}, and is {cat_oldest.age} years old.")


# Exercice 2: Dogs
class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        # Fix: ajout de "cm high!" comme demandé dans les instructions
        print(f"{self.name} jumps {self.height * 2} cm high!")

# Step 2: Create Dog Objects
davids_dog = Dog("Rex", 45)
sarahs_dog = Dog("Bella", 85)

# Step 3: Print Dog Details and Call Methods
print(f"David's dog: name={davids_dog.name}, height={davids_dog.height}cm")
print(f"Sarah's dog: name={sarahs_dog.name}, height={sarahs_dog.height}cm")

# Fix: appels manquants à bark() et jump() pour chaque chien
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print("the bigger dog is", davids_dog.name)
else:
    print("the bigger dog is", sarahs_dog.name)


# Exercice 3: Who's the song producer?
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)

stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()


# Exercice 4: Afternoon at the Zoo
class Zoo():
    # Fix: __init__ ne prend que zoo_name — animals initialisé en liste vide en interne
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    # Bonus: *args pour ajouter plusieurs animaux en un seul appel
    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal in self.animals:
                print(f"{animal} already exists!")
            else:
                self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        dictionaire = {}
        for animal in self.animals:
            premiere_lettre = animal[0].upper()
            if premiere_lettre not in dictionaire:
                dictionaire[premiere_lettre] = []
            dictionaire[premiere_lettre].append(animal)
        return dict(sorted(dictionaire.items()))

    def get_groups(self):
        # Fix: self.sort_animals() au lieu de zoo1.sort_animals()
        for letter, liste in self.sort_animals().items():
            print(f"{letter}: {liste}")

# Step 2: Create a Zoo instance — Fix: plus besoin de passer la liste en paramètre
zoo1 = Zoo("ZooName")

# Step 3: Use the Zoo methods
# Bonus en action: ajout de plusieurs animaux en un seul appel
zoo1.add_animal('Giraffe', 'Cat', 'Cougar', 'Lion', 'Zebra', 'Baboon', 'Bear', 'Leopard')
zoo1.add_animal("Dog")
zoo1.get_animals()
zoo1.sell_animal("Cat")
zoo1.get_animals()
print(zoo1.sort_animals())
zoo1.get_groups()