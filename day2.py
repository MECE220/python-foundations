# Variables
name = "Reiko"
age = 25
height = 5.7
is_engineer = True

print(name)
print(age)
print(height)
print(is_engineer)

# Strings — text, always in quotes
my_name = "Reiko"
my_course = 'Mechatronics'          # single or double quotes both work
greeting = f"My name is {my_name}"  # f-string: embed variables inside text
print(greeting)

# Integers — whole numbers
score = 95
year = 2025
print(score + year)

# Floats — decimal numbers
gpa = 3.85
pi = 3.14159
print(round(pi, 2))  # round to 2 decimal places

# Booleans — True or False only
is_employed = False
has_degree = True
print(is_employed)
print(has_degree)

# LIST — ordered collection of items (like an array)
skills = ["Python", "Git", "Linux", "SQL"]
print(skills)
print(skills[0])       # first item — indexing starts at 0
print(skills[-1])      # last item
print(len(skills))     # how many items

skills.append("Docker")  # add to the end
print(skills)

# Loop through a list
for skill in skills:
    print("Learning:", skill)

# DICTIONARY — key-value pairs (like a labeled box)
profile = {
    "name": "Juan",
    "age": 23,
    "degree": "Mechatronics",
    "target_company": "Oracle"
}

print(profile["name"])           # access by key
print(profile["target_company"])

profile["employed"] = False      # add a new key
print(profile)

# Loop through a dictionary
for key, value in profile.items():
    print(f"{key}: {value}")