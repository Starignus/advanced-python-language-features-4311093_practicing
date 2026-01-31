# Example file for Advanced Python: Language Features by Joe Marini
# define enumerations using the Enum base class

"""
Docstring for Start.Ch_4.enums_start

Python supports enumerations just like other popular programming languages,
 and they're useful in a variety of scenarios. Usually, they're used to 
 assign easy-to-read names to constant values in a program which helps to 
 increase the readability of your code. They can also be used as hash values, 
 and you can iterate over them like you would other iterables in Python. 
 Enumerations are defined using the class syntax. 

 With Enums is not valud to have duplicate names, but you can duplciate values
"""


from enum import Enum, unique, auto

# TODO: enums have human-readable values and types
@unique #decorator to prevent duplicate values
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    PEAR = 4
    GRAPE = 5

# TODO: enums have name and value properties
print(Fruit.APPLE)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))

print(Fruit.APPLE.name)
print(Fruit.APPLE.value)

# If you do not que what the values are, you can use auto()
# TODO: print the auto-generated value
class Animal(Enum):
    DOG = auto()
    CAT = auto()
    BIRD = auto()
    FISH = auto()

print(Animal.DOG.value)
print(Animal.CAT.value)
print(Animal.BIRD.value)
print(Animal.FISH.value)

# TODO: enums are hashable - can be used as keys
my_fruits = {}
my_fruits[Fruit.APPLE] = "A red fruit"
my_fruits[Fruit.BANANA] = "A yellow fruit"
print(my_fruits[Fruit.APPLE])