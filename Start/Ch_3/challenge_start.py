# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions
"""
Docstring for Start.Ch_3.challenge_start

Use comprehensions to process a string
Given an input string, use comprehensions to determine the following characteristics:
	- The number of numeric characters in the string
	- The number of punctuation characters in the string
	-The number of unique letters in the string
	- A string that contains only the unique alphabetic characters in the original string
Also, determine the length of the string itself.

Parameters:

Your code will be given a sample string, such as:

test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg,
Jane's i kiwis, $50!"

Result:

Your code will calculate the following values:

l: the length of the string
num_chars: the number of numeric characters in the string 
num_punct: the number of punctuation characters in the string 
num_unique: the number of unique characters in the string 
unique_str: the string containing only the unique alphabetic characters

These global variables are defined for you. You don't need to return a value from the function, just set these values appropriately.

Constraints
• The string always contains at least one character.


"""


import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

def cal_values(the_str):
    """
    Docstring for cal_values

    the_str: input string to be processed
    returns: tuple containing calculated values:
        l: length of the string
        num_char: number of numeric characters in the string
        num_punct: number of punctuation characters in the string
        num_unique: number of unique alphabetic characters in the string
        unique_str: string containing only the unique alphabetic characters from the input string
    Exceptions:
        Raises AssertionError if the input string is empty.
    """
    try:
        assert len(the_str) > 0
    except AssertionError as e:
        print("Input string must contain at least one character.")
        raise e
    else:
    # print the data
    # we can use as well len instrad of sum once used the list comprehension
      str_data = {
      "l": len(the_str),
      # len([c for c in the_str if c.isnumeric()]),
      "num_char": sum(1 for c in the_str if c.isnumeric()),
      # len([c for c in the_str if c in string.punctuation]),
      "num_punct": sum(1 for c in the_str if c in string.punctuation),
      # num_unique calcuated as len(unique_str)
      "num_unique": sum(1 for c in set(the_str) if c.isalpha()),
      "unique_str": "".join(c for c in set(the_str) if c.isalpha() )
    }
      return str_data["l"], str_data["num_char"], str_data["num_punct"], str_data["num_unique"], str_data["unique_str"]

  




pprint.pp(cal_values(test_str))

