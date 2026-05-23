# Exercice 1: Pets

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Siamese(Cat):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


bengal_obj = Cat("mimi", 10)
chartreux_obj = Cat("michou", 7)
siamese_obj = Siamese("milou", 11, "Siamese")  
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats)
sara_pets.walk()


# Exercice 2: Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        run_speed = self.run_speed()
        other_run_speed = other_dog.run_speed()
        if run_speed * self.weight > other_run_speed * other_dog.weight:
            print(f"{self.name} won the fight")
        elif run_speed * self.weight < other_run_speed * other_dog.weight:
            print(f"{other_dog.name} won the fight")
        else:
            print("It's a draw!")  

dog1 = Dog("Rex", 5, 25)
dog2 = Dog("Max", 10, 35)
dog3 = Dog("Thor", 15, 40)

print(dog1.bark())
print(dog2.run_speed())
dog3.fight(dog2)