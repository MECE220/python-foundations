# CONDITIONASL - if, elif, else

age = 25

if age >= 18:
    print("You are an adult.")
else: 
    print("You are a minor.")

# Multiple conditions with elif
score = 95

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade= "D"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")

# Comparison operators: == != > < >= <=
# Logical operators: and, or, not

temperature = 20
is_raining = True

if temperature > 20 and is_raining:
    print("Hot and rainy - stay inside.")
elif temperature > 20 and not is_raining:
    print("Hot and sunny - go outside.")
elif temperature <= 20 and is_raining:
    print("Cool and rainy - bring an umbrella.")
else:
    print("Cool and dry - perfect weather.")
    
# FOR LOOP - repeat for each item in a collection
skills =["Python", "Git", "SQL", "Docker", "Spark"]

for skill in skills:
    print(f"Learning: {skills}")

# range(start, stop, step)
print("Counting up:")
for i in range(1, 6):
    print(i)

print("Counting down:")
for i in range(10, 0, -2):
    print(i)

# WHILE LOOP - repeat until condition is FALSE
energy = 5

while energy > 0:
    print(f"Studying... energy level: {energy}")
    energy -= 1 # same as energy = energy - 1
print("Out of energy. Time to sleep")

# Loops + conditionals together
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_number = []
odd_number = []

for num in number:
    if num % 2 == 0:   # % is the modulo operator - gives the remainder, The % (modulo) operator gives the remainder after division — if dividing by 2 gives remainder 0, the number is even. You'll use this pattern constantly.
        even_number.append(num)
    else:
        odd_number.append(num)

print("Even:", even_number)
print("Odd:", odd_number)

# FUNCTIONS - define once, use many times

# Basic function - no input, no output
def greet():
    print("Hello, welcome to your Python journey.")
    
greet() # call the function
greet() # call it again - same code, runs twice

# Function with parameters - accepts input
def greet_person(name):
    print(f"Hello, {name}! Great to meet you.")

greet_person("Reiko")
greet_person("Oracle Recuiter")

# Function with return value - produces output
def add(a, b):
    result = a + b 
    return result

total = add(10, 25)
print(f"10 + 25 = {total}")

# Funtion with default parameters
def introduce(name, role ="Student"):
    print(f"I am {name}, currently a {role}.")
    
introduce("Reiko")
introduce("Reiko", "Junior Data Engineer")

# def →keyword that defines a funciton
# greet → the name you give it
# (name) → parameter: inputs the funciton accepts
# return → sens a value back to whoever called the function