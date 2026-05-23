# Exercice 3:Dogs Domesticated

from mandatory import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())        
        self.trained = True

    def play(self, *args):
        names = ", ".join(dog.name for dog in args)
        print(f"{self.name}, {names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")


# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
buddy = PetDog("Buddy", 3, 12)
max_dog = PetDog("Max", 4, 15)

my_dog.train()
my_dog.play(buddy, max_dog)   
my_dog.do_a_trick()


# Exercice 4: Family and Person Classes

class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


# ✅ FIX: Family n'hérite PAS de Person (pas de lien logique)
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []          # ✅ FIX: liste dans __init__, pas en argument par défaut

    def born(self, first_name, age):
        new_person = Person(first_name, age, self.last_name)
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if first_name == member.first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return                 # ✅ FIX: on sort dès qu'on a trouvé le membre
        print("member not exist")      # ✅ FIX: affiché seulement si personne trouvée

    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, age is {member.age}")  # ✅ FIX: .age au lieu de .last_name


# Test
family = Family("Dupont")
family.born("Alice", 20)
family.born("Tom", 15)
family.born("Emma", 18)

family.family_presentation()
family.check_majority("Alice")
family.check_majority("Tom")
family.check_majority("Bob")


