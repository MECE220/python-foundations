# Import from Python's built-in standard library
import math
import random
import datetime
import os

# math module
print("=== MATH===")
print(math.pi)              # 3.14159...
print(math.sqrt(144))       # 12.0
print(math.pow(2, 10))      # 1024.0
print(math.ceil(4.5))       # 5 - round up
print(math.floor(4.9))      # 4 - round down

# random module
print("\n=== RANDOM ===")
print(random.randint(1, 100))   # random number 1-100
print(random.choice(["Python", "Java", "SQL", "Spark"]))    # random item
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)      # shuffle in place
print(numbers)

# datetime module
print("\n=== DATETIME ===")
now = datetime.datetime.now()
print(now)          # current date and time
print(now.year)
print(now.strftime("%B %d, %Y"))    # formatted: "Januray 01, 2026"

# os module
print("\n=== OS ===")
print(os.getcwd())      # current working directory
print(os.listdir('.'))  # files in current folder