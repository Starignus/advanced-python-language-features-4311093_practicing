# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use set comprehensions


# define a list of temperature data points
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

# TODO: build a set of unique Fahrenheit temperatures
ftemps1 = [(t * 9/5) + 32 for t in ctemps]
print(ftemps1)

# Unique value using set comprehension
ftemps = {(t * 9/5) + 32 for t in ctemps}
print(ftemps)

# TODO: Count he unique letters while converting them to uppercase and not taking accoint spaces
# s_temp = "The quick brown fox jumped over the lazy dog"
s_temp = "Test the case"
unique_letters = {char.upper() for char in s_temp if not char.isspace()}
print(unique_letters)
print(len(unique_letters))
unique_letters_aapended = "".join(unique_letters)
print(unique_letters_aapended)
# If we want to sort them to keep the order consistent, but it is not a set anymore
unique_letters_sorted = sorted(unique_letters) 
print(type(unique_letters_sorted))
print("".join(unique_letters_sorted))