"""
Example file for Advanced Python: Language Features by Joe Marini
Challenge solution file for Advanced Functions

Challenge:
Write a function that performs the following actions:
1: accepts a variable number of strings and integers. Other types ignored
2: accepts a keyword-only argument to return a unique-only result
3: combines all the arguments into a single string
4: returns a string containing all arguments combined as one string
5: Has a docstring that explains how it works
If the unique-only argument is True (default False), then the result
combined string will not contain any duplicate characters

Parameters:

def string_combiner(*args, unique=False):

args: A list of values which can be variables in length
unique: True if the result string should contain only unique values

Result:
string: The resulting string which is a combination of all the function arguments
into a single string result

Constraints:
The args list always contains at least one value
"""


def string_combiner(*args, unique=False):
    """
    Docstring for string_combiner
    
    args:  list of values which can be variables in length
    unique: True if the result string should contain only unique values

    retunrs:
    string: The resulting string which is a combination of all the function arguments
    into a single string result. If unique is True, the string contains only unique characters.
    """
    result = ""
    for item in args:
        if isinstance(item, str) or isinstance(item, int):
            result += str(item)

    if unique:
        result = "".join(set(result))
    return result 

# test code:
print(string_combiner.__doc__)
print()
output = string_combiner("This", "is", 1, "test", "string!", unique=False)
print(output)
# Thisis1teststring!
output = string_combiner("This", "is", 1, "test", "string!", unique=True)
print(output)
# enti1r!shTg
output = string_combiner("This", "is", 1, True, "string!", unique=False)
print(output)
# Thisis1Truestring!
output = string_combiner("This", "is", [1, 2], "string!", unique=False)
print(output)
# Thisisstring!
