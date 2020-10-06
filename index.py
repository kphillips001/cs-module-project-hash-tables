records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]
​
​
def build_index(records):
    idx = {}
    # Build a dict where the keys are: departments
    # the values are: LISTS of names
​
    # loop through the records at least once
    for record in records:
        name = record[0]
        department = record[1]
​
        # the department might not exist yet in the dictionary
        if department not in idx:
            idx[department] = [name] 
        else:
        # or the department already exists
            idx[department].append(name)
​
    return idx
​
​
index_dict = build_index(records)
print(index_dict)
​
def print_department_using_index(dep_name):
    print(index_dict[dep_name])
​
​
print_department_using_index("Engineering")
print_department_using_index("Marketing")
print_department_using_index("Sales")
# [Alice, Dave, Erin, Frank]