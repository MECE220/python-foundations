# Variables
name = "Reiko Paulo A. Feckleng"
age = "25"
height = "5.7"
is_engineer = "true"

print(name)
print(age)
print(height)
print(is_engineer)

# Strings - text, always in quotes
my_name = "Reiko Paulo A. Feckleng"
my_course = 'Mechatronics Engineer'      # single or double quotes can be used for strings/ both work
greeting = f"My name is {my_name}" # f-string allows you to embed expressions inside string literals, using curly braces {}. The expression inside the brace is evaluated at runtime and the formatted string is returned. 
                                # f-string: embed variables inside text
print(greeting)

# Integers - whole numbers
score = 95
year = 2025
print(score and year) # addition of two integers

# Floats - decimal numbers
gpa = 3.85
pi = 3.14159
print(round(pi, 2)) # round function rounds the value of pi to 2 decimanl places

# Booleans - true or false values
is_employed = False
has_degree = True
print(is_employed)
print(has_degree)

# List - ordered collection of items (like an array)
skills = ["Pyhton", "Git", "Linux", "SQL",]
print(skills)
print(skills[0]) # first item - indexing starts at 0
print(skills[-1]) #last item - negative indexing starts from the end
print(len(skills)) # how many items

skills.append("Docker") # add to the end
print(skills)

# Loop through a list
for skills in skills:
    print("Learning:", skills)

# DICTIONARY - key-value pairs (like a labeled box)
profile = {
    "name": "Reiko Paulo A. Feckleng",
    "age": 25,
    "degree": "Mechatronics Engineer",
    "target_company": "Oracle"
}

print(profile["name"]) # access by key
print(profile["target_company"])

profile["employed"] = False # add a new key
print(profile)

# Loop through a dictionary
for key, value in profile.items():
    print(f"{key}: {value}")
    