#Exercice 1

# def new_decorator(func):
#     def wrap_func():
#         print("code before func!")
#         func()
#         print("code after func!")
#     return wrap_func

# def decorate_me():
#     print("decorate me!")

# decorate_me = new_decorator(decorate_me)

# decorate_me() # What do you think this will print?

# Exercice 2

# def new_decorator(func):
#     def wrap_func():
#         print("code before func!")
#         func()
#         print("code after func!")
#     return wrap_func

# @new_decorator
# def decorate_me():
#     print("decorate me!")

# Exercice 3
# import datetime


# def my_decorator(inner):
#     def inner_decorator(num_copy):
#         print(datetime.datetime.utcnow())
#         inner(int(num_copy) + 1)
#         print(datetime.datetime.utcnow())
#     return inner_decorator


# @my_decorator
# def decorated(number):
#     print("This happened : " + str(number))

# decorated(5)

# Exercice 4
class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = val
        MyClass.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count

object_1 = MyClass(10)
print("\nValue of object : %s" % object_1.get_val())
print(MyClass.get_count())

object_2 = MyClass(20)
print("\nValue of object : %s" % object_2.get_val())
print(MyClass.get_count())


#Exercice 5

class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        MyClass.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            print("Entered value is not an INT, value set to 0")
            return 0
        else:
            return value


a = MyClass(5)
b = MyClass(10)
c = MyClass(15)

print(a.val)
print(b.val)
print(c.val)
print(a.filterint(100))
