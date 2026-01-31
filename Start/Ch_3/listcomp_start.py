# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# TODO: Perform a mapping and filter function on a list
evens_squared = list(map(lambda e: e**2, evens))
print(evens)
# filterin 
evens_squared = list(map(lambda e: e ** 2, filter(lambda e: e > 4 and e < 16, evens)))
print(evens_squared)


# TODO: Derive a new list of numbers frm a given list
events_squared_lc = [e ** 2 for e in evens if e > 4 and e < 16]
print(events_squared_lc)

# TODO: Limit the items operated on with a predicate condition
events_odds_lc = [e ** 2 for e in odds if e > 3 and e <17]
print(events_odds_lc)