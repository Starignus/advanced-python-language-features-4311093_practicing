# Example file for Advanced Python: Language Features by Joe Marini
# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person Class - fname: {self.fname}, lname: {self.lname}, age: {self.age}>"

    # TODO: use str for a more human-readable string
    def __str__(self):
        return f"Person {self.fname} {self.lname} is {self.age}"
    
    def __bytes__(self):
        # it can be alxo wirten as:bytes(f"{self.fname} : {self.lname} : {self.age}".encode('utf-8'))
        return bytes(f"{self.fname} : {self.lname} : {self.age}", 'utf-8')


# create a new Person object
cls1 = Person()

# use different Python functions to convert it to a string
print(repr(cls1))
print(str(cls1))
print(f"Formatted: {cls1}")
print(bytes(cls1))


# print the object directly without modifying the code
# <__main__.Person object at 0x104c320f0>
# <__main__.Person object at 0x104c320f0>
# Formatted: <__main__.Person object at 0x104c320f0>

# Now with __repr__ that was overridden
# <Person Class - fname: Joe, lname: Marini, age: 25>
# <Person Class - fname: Joe, lname: Marini, age: 25>
# Formatted: <Person Class - fname: Joe, lname: Marini, age: 25>

# Now with __str__ that was overridden
# <Person Class - fname: Joe, lname: Marini, age: 25>
# Person Joe Marini is 25
# Formatted: Person Joe Marini is 25

# Now with __bytes__ that was overridden
# <Person Class - fname: Joe, lname: Marini, age: 25>
# Person Joe Marini is 25
# Formatted: Person Joe Marini is 25
# b'Joe : Marini : 25'