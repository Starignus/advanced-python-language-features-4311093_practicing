# Example file for Advanced Python: Language Features by Joe Marini
# Using pattern guards to restrict how matches are made

# define some geometric shapes
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return 3.14 * (self.radius ** 2)


class Square:
    def __init__(self, side):
        self.side = side

    def getarea(self):
        return self.side * self.side


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height


# create a list of some shapes
shapes = [Circle(5), Square(4), Rectangle(4, 6),
          Square(7), Circle(9), Rectangle(2, 5), 
          Rectangle(5, 5)]

# use pattern matching to process each shape
# include pattern guards for more detailed processing
for shape in shapes:
    match shape:
        # TODO: add a pattern guard for Circle
        # It is inportaant to note that the order of the cases matters when using pattern guards. 
        # The more specific case with the guard should come before the more general case 
        # to ensure that it is evaluated first. If the more general case were placed before the specific case,
        #  it would match all Circle instances, including those with a radius greater than 6,
        #  and the specific case with the guard would never be reached.
        case Circle(radius=r) if r > 6: # the r >6 serves as a pattern guard to restrict the match to only circles with radius greater than 6.
            print(f"Large Circle with area {shape.getarea()}")
        case Circle():
            print(f"Circle with area {shape.getarea()}")
        case Square():
            print(f"Square with area {shape.getarea()}")
        case Rectangle(width=w, height=h) if w==h: # the w==h serves as a pattern guard to restrict the match to only rectangles that are actually squares (where width and height are equal).:
            print(f"Square with area {shape.getarea()}")
        case Rectangle():
            print(f"Rectangle with area {shape.getarea()}")
        case _:
            print(f"Unrecognized shape: {type(shape)}")

print()
# TODO: Pattern guards can get fairly sophisticated
dataset = ["UPPER", 5, "Mixed Case", True, None]
for d in dataset:
    match d:
        case str() as s if s.isupper():
            print(f"{d} is all uppercase")
        case str():
            print(f"{d} is a string but not all uppercase")
        case bool(): # In Python, bool is a subclass of int, so it is important to check for bool before int if you want to distinguish between them.
            print(f"{d} is a boolean")
        case odd if isinstance(d, int) and d % 2 != 0: # This case uses a pattern guard to check if the value is an odd integer. The isinstance(d, int) check ensures that d is an integer before checking if it is odd.
            print(f"{d} is an odd integer")
        case int(): 
            print(f"{d} is an integer")
        case _:
            print(f"{d}: Something else")
