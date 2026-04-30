# utils.py
# Reusable utility functions  for your projects

def get_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: "C"
    elif score >= 60: return "D"
    else: return "F"
    
def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:,.2f}"

def calculate_percentage(part, total):
    if total == 0:
        return 0
    return round((part / total) * 100, 2)

def print_header(title, width=45):
    print("=" * width)
    print(f" {title.upper()}")
    print("=" * width)
    
def clamp(value, min_val, max_val):
    """Keep a value within a range - used everywhere in data validation"""
    return max(min_val, min(max_val, value))

# Import your own module
import utils

print("\n=== USING UTILS MODULE ===")
utils.print_header("My Utility Functions")
print(utils.get_grade(88))
print(utils.format_currency(1500.5))
print(utils.calculate_percentage(45, 200))
print(utils.clamp(150, 0, 100))     # clamps 150 down to 100