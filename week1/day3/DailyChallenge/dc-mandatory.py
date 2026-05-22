# Instructions: Old MacDonald's Farm
# You are given example code and output. Your task is to create a Farm class that produces the same output.

class Farm(): #Create the Farm Class
    def __init__(self, farm_name): #Implement the __init__ Method
        self.name = farm_name
        self.animals = {}

    # Step 8: **kwargs allows passing multiple animals at once
    # e.g. farm.add_animal(cow=5, sheep=2) OR farm.add_animal('pig', 3)
    def add_animal(self, animal_type=None, count=1, **kwargs): #Implement the add_animal Method
        # Handle single animal (original behaviour preserved)
        if animal_type is not None:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count

        # Handle multiple animals via kwargs
        for animal, qty in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += qty
            else:
                self.animals[animal] = qty

    def get_info(self): # Implement the get_info Method — Step 4 fix: return string + correct format
        lines = [f"{self.name}'s farm", ""]
        for animal, count in self.animals.items():
            lines.append(f"{animal:<10} : {count}")
        lines.append("")
        lines.append("    E-I-E-I-0!")  # Note: '0' is a zero, not the letter O
        return "\n".join(lines)

    def get_animal_types(self):  # Step 6
        return sorted(self.animals)

    def get_short_info(self):  # Step 7 fix: fully dynamic, uses return
        animal_types = self.get_animal_types()
        plural_animals = [
            animal + "s" if self.animals[animal] > 1 else animal
            for animal in animal_types
        ]
        animals_str = ", ".join(plural_animals[:-1]) + " and " + plural_animals[-1]
        return f"{self.name}'s farm has {animals_str}."


# Test Your Code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

print(macdonald.get_short_info())

# Step 8 — kwargs usage
macdonald.add_animal(pig=3, horse=1)
print(macdonald.get_info())
