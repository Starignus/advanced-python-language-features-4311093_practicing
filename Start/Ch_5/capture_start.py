# Example file for Advanced Python: Language Features by Joe Marini
# Capture pattern matching for assigning values within the match

name = input("What is your name? ")

match name:
    case "":
        print("Hello, anonymous!")
    case "Joe" | "Joseph" as a:
        print(f"Print the name, {a}!")
    case name:
        print(f"Hello, {name}!")