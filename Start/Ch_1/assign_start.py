# Example file for Advanced Python: Language Features by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
x = 5
print(x)

# TODO: the assignment operator is part of an expression

(x := 10) # helps to the readability 
print(x)

# TODO: The assignment expression is useful for writing concise code
# thestr = input("Value?:")
# while thestr != "exit":
#     print(f"You entered: {thestr}")
#     thestr = input("Value?:")
# can be rewritten using the walrus operator

# while (thestr := input("Value?:")) != "exit":
#     print(f"You entered: {thestr}")


# TODO: The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    "length": len(values),
    "total": sum(values),
    "average": sum(values) / len(values)
}

pprint.pp(val_data)


# can be rewritten using the walrus operator
val_data = {
    "length": (n := len(values)),
    "total": (t := sum(values)),
    "average": t / n
}
pprint.pp(val_data)