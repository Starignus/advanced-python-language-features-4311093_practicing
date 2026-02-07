# Example file for Advanced Python: Language Features by Joe Marini
# Sequence pattern matching example - matches against value sequences

import math


# Set up some test data with different math operations
operations = [
    ["Add", 1, 2, 3, 4, 5],
    ["Mul", 5, 6],
    ["Add", 10, 20],
    ["Sqrt", 9],
]

result = 0

# TODO: process each operation along with the set of given numbers
for op in operations:
    match op:
        case "Mul", num1, num2:
            result = num1 * num2 # it has fixed length of 2 numbers.
        case "Sqrt", num1:
            result = math.sqrt(num1) # it has fixed length of 1 number.
        case "Add", *nums: # it has variable length of numbers.
            result = sum(nums)
        case _:
            continue

    print(f"{op}: {result}")

# It I add a number to the "Mul" operation, it will no longer match the pattern and will be ignored


# We can modify and obtain the same

for op in operations:
    match op:
        case "Mul", num1, num2:
            result = num1 * num2 # it has fixed length of 2 numbers.
        case "Sqrt", num1:
            result = math.sqrt(num1) # it has fixed length of 1 number.
        case "Add", num1, *nums: # it has variable length of numbers and at least there should be one number.
            result = num1 + sum(nums)
        case _:
            continue

    print("Modified")        
    print(f"{op}: {result}")