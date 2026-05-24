import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    # définir un cercle par son diamètre via un classmethod decorator
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    # lire/écrire le diamètre via une property decorator
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return (f"Circle — radius: {self.radius:.2f}, "
                f"diameter: {self.diameter:.2f}, "
                f"perimeter: {self.perimeter():.2f}, "
                f"area: {self.area():.2f}")

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented


# ── Tests ──────────────────────────────────────────────
circle1 = Circle(5)
circle2 = Circle(7)

# Créer via diamètre
circle_from_d = Circle.from_diameter(14)
print(f"Créé depuis diamètre 14 → {circle_from_d}")

# __str__
print(circle1)

# __add__
circle3 = circle1 + circle2
print(f"circle1 + circle2 = {circle3}")

# __gt__
print(f"circle1 > circle2 : {circle1 > circle2}")   # False
print(f"circle2 > circle1 : {circle2 > circle1}")   # True

# __eq__
print(f"circle3 == circle2 : {circle3 == circle2}")  # False (12 != 7)
print(f"Circle(7) == circle2 : {Circle(7) == circle2}")  # True

# __lt__ + sorted() 
circles = [Circle(9), Circle(3), Circle(6), circle1, circle2]
sorted_circles = sorted(circles)
print("\nCercles triés par rayon :")
for c in sorted_circles:
    print(f"  {c}")