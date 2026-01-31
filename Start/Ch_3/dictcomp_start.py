# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use dictionary comprehensions


# define a list of temperature values
ctemps = [0, 12, 34, 100]

# TODO: Use a comprehension to build a dictionary

temp_fahr = {c: (c * 9/5) + 32 for c in ctemps}
print(temp_fahr)
print(temp_fahr[12])

# TODO: Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}

# The first FOR give us a team from the tuple, the second FOR gives the key,value for each item in each team
team_merged = {player: team_num for team in (team1, team2) for player, team_num in team.items()}
print(team_merged)