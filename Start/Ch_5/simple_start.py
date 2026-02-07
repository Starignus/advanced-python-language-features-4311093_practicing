# Example file for Advanced Python: Language Features by Joe Marini
# Simple pattern matching using literal values

x = "Zero"

# TODO: Literal patterns are explicit values: integers, strings, Booleans, etc
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case "Zero":
        print("x is zero as a string")
    case None:
        print("x is None")
    case _: # the default case, matches anything not matched by the previous cases
        print("x is something else, no mathcing case found")