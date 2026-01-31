# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions


# TODO: define a function that takes variable arguments
def addition(*args):
    print(args, type(args))    
    resoult = 0
    for arg in args:
        resoult += arg
    return resoult


def addition2(base, **kwargs):
    resoult = base
    for key in kwargs:
        resoult += kwargs[key]
    return resoult

# TODO: pass different arguments and use the unpacking operator
my_nums = [1, 2, 3, 4, 5]
print(addition(*my_nums))

# TODO: pass an existing list
other_nums = [10, 20, 30]
print(addition(*other_nums))

print(addition(4,5,6,7,8))
# This will fail because addition only takes positional arguments.
# so we need to use the unpacking operator carefully with small number of args
print(addition2(100,*other_nums))