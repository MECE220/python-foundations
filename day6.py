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

# requests — fetch data from the internet
import requests

print("\n=== REQUESTS — LIVE DATA ===")
try:
    response = requests.get("https://api.github.com/users/MECE220")
    if response.status_code == 200:
        data = response.json()
        print(f"GitHub user : {data['login']}")
        print(f"Public repos: {data['public_repos']}")
        print(f"Followers   : {data['followers']}")
    else:
        print(f"Error: Status code {response.status_code}")
except requests.exceptions.ConnectionError:
    print("No internet connection")
    
# rich — beautiful terminal output
from rich.console import Console
from rich.table import Table

console = Console()

print("\n=== RICH — BEAUTIFUL OUTPUT ===")

# Colored text
console.print("Hello [bold green]Oracle[/bold green]!", style="bold")
console.print("[red]Error:[/red] Something went wrong", style="")
console.print("[blue]Info:[/blue] Process completed successfully")

# Beautiful table
table = Table(title="My Learning Progress")
table.add_column("Day", style="cyan", width=6)
table.add_column("Topic", style="white", width=25)
table.add_column("Status", style="green", width=12)

table.add_row("1", "Environment Setup", "✓ Done")
table.add_row("2", "Variables & Data Types", "✓ Done")
table.add_row("3", "Loops & Functions", "✓ Done")
table.add_row("4", "Error Handling & Files", "✓ Done")
table.add_row("5", "OOP", "✓ Done")
table.add_row("6", "Modules & Libraries", "✓ Done")

console.print(table)