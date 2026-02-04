# Example file for Advanced Python: Language Features by Joe Marini
# Use special methods to compare objects to each other


class Employee():
    def __init__(self, fname, lname, level, years_service):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = years_service

    # TODO: implement comparison functions by emp level
    def __ge__(self, other): # Who is more senior
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level    

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level

# define some employees
dept = []
dept.append(Employee("Tim", "Sims", 5, 9))
dept.append(Employee("John", "Doe", 4, 12))
dept.append(Employee("Jane", "Smith", 6, 6))
dept.append(Employee("Rebecca", "Robinson", 5, 13))
dept.append(Employee("Tyler", "Durden", 5, 12))

# TODO: Who's more senior?
# Answer beofre adding the years of service consideration when levels are the same
# Befoire the "/" 
print(dept[0] > dept[2]) # False bc 5 > 6 is false / False bc 9 > 6 is false
print(dept[4] < dept[3]) # False bc 5 < 5 is false / True bc 12 < 13 is true
print(dept[4] >= dept[0]) # True bc 5 >= 5 is true / True because 12 >= 9 is true
print(dept[2] <= dept[3]) # False bc 6 <= 5 is false / False because 6 <= 13 is false
print(dept[1] == dept[4]) # False bc 4 == 5 is false / 


# TODO: sort the items

for emp in dept:
    print(f"employee: {emp.lname}")
print("----- sorting now -----")
emps_sorted = sorted(dept, reverse=False) # from least senior to most senior
for emp in emps_sorted:
    print(f"employee: {emp.lname}")

"""
When dept.append(Employee("Rebecca", "Robinson", 5, 13))


employee: Sims
employee: Doe
employee: Smith
employee: Robinson
employee: Durden
----- sorting now -----
employee: Doe
employee: Sims
employee: Durden
employee: Robinson
employee: Smith

Wehn dept.append(Employee("Rebecca", "Robinson", 5, 11))

employee: Sims
employee: Doe
employee: Smith
employee: Robinson
employee: Durden
----- sorting now -----
employee: Doe
employee: Sims
employee: Robinson
employee: Durden
employee: Smith
"""