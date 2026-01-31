# Example file for Advanced Python: Language Features by Joe Marini
# customize string representations of objects



class MyColor():
    def __init__(self):
        # This has three regular attributes
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{:02x}{:02x}{:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError(f"'MyColor' object has no attribute '{attr}'")

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, value):
        if attr == "rgbcolor":
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        else:
            # The code arealdy set some attrute values in __init__
            # and seterr will be called evry time we set an attribute
            # call the superclass to actually set the value
            # to avoid infinite recursion we need to call the superclass
            # in the else block. In that way the initalisation attributes
            # continues to work, otherweise they won't be set.
            super().__setattr__(attr, value)

    # TODO: use dir to list the available properties
    def __dir__(self):
        return ("rgbcolor", "hexcolor")


# create an instance of myColor
cls1 = MyColor()
# TODO: print the value of a computed attribute
print(cls1.rgbcolor)
print(cls1.hexcolor)
# TODO: set the value of a computed attribute
cls1.rgbcolor = (200, 150, 100)
print(cls1.rgbcolor)
print(cls1.hexcolor)

# TODO: access a regular attribute
print(cls1.red)
# TODO: list the available attributes
print(dir(cls1))