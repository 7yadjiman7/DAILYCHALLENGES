# Exercice 1:  Geometry
import math
class Circle():
    def __init__(self,radius=1.0):
        self.radius = radius
    
    def perimeter(self):
        return 2*math.pi*self.radius
    
    def area(self):
        return math.pi*self.radius**2
    
    def geoDefinition(self):
        print("the geomertical definition of circle is: the Circle is a set of all points located at the same distance (called the radius) froma fixed point (called the center)")


circle1 = Circle(3.0)
print(circle1.perimeter())
print(circle1.area())
circle1.geoDefinition()

# Exercice 2:Custom List Class
import random
class MyList():
    def __init__(self,letter_list):
        self.letter_list = letter_list
    
    def reverse(self):
        return sorted(self.letter_list, reverse=True)
    
    def sort(self):
        return sorted(self.letter_list)
    
    def new_list(self):
        new_list = []
        for i in range(len(self.letter_list)):
            new_list.append(random.randint(1,len(self.letter_list)))
        
        return new_list

list_letter = ["a","b","g","t","p","q","z"]
mylist = MyList(list_letter)
print(mylist.reverse())
print(mylist.sort())
print(mylist.new_list())

# Exercice 3:Restaurant Menu Manager

class MenuManager():
    def __init__(self):
        self.menus = [{"name": "Soup","price": 10,"spice level": "B","gluten index": False},
                     {"name": "Hamburger ","price": 15,"spice level": "A","gluten index": True},
                     {"name": "Salad","price": 18,"spice level": "A","gluten index": False},
                     {"name": "French Fries","price": 5,"spice level": "C","gluten index": False},
                     {"name": "Beef bourguignon","price": 25,"spice level": "B","gluten index": True}]
        
    def add_item(self,name, price, spice, gluten):
            dictionary = {"name": name,"price": price,"spice level": spice,"gluten index": gluten}
            self.menus.append(dictionary)
        
    def update_item(self,name, price, spice, gluten):
        dictionary = {"name": name,"price": price,"spice level": spice,"gluten index": gluten}
        for i in range(len(self.menus)):
            if name == self.menus[i]["name"]:
                self.menus[i] = dictionary
                print(self.menus)
                return
        print("dish isn't in the menu")
            
    def remove_item(self,name):
        for i in range(len(self.menus)):
            if name == self.menus[i]["name"]:
                self.menus.pop(i)
                print(self.menus)
                return
        print("dish isn't in the menu")    
            
MenuManger = MenuManager()
MenuManger.add_item(name="attiéké", price=20, spice="A", gluten=True)
MenuManger.update_item(name="Soup",price=50,spice="B", gluten=False)
MenuManger.remove_item("Salad")