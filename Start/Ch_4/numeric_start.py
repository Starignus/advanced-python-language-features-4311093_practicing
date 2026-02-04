# Example file for Advanced Python: Language Features by Joe Marini
# give objects number-like behavior


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point x:{self.x},y:{self.y}>"

    # TODO: implement addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # TODO: implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    # TODO: implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


# Declare some points
p1 = Point(10, 20)
p2 = Point(30, 30)
print(p1, p2)

# TODO: Add two points
# default without modification in the code
print(p1 + p2) # if commented out the __add__ method this will raise an error

# TODO: subtract two points
print(p2 - p1)

# TODO: Perform in-place addition
p1 += p2
print(p1)
