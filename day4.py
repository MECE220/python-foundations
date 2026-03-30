# Basic try/except
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
print("Program continues running...")

# Handling different error types
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Both inputs must be numbers."
print(safe_divide(10, 2))   # works fine
print(safe_divide(10, 0))   # zero division → error message
print(safe_divide(10, "hello")) # wrong type → error message

# else runs if NO error occured
# finally runs NO MATTER WHAT - error or not
def convert_to_int(value):
    try:
        number = int(value)
    except ValueError:
        print(f" '{value}' cannot be converted to an integer.")
    else:
        print(f" Successfully converted: {number}")
    finally:
        print(f" Attempted to conversion of: '{value}'")

print("--- Conversion Attempts ---")
convert_to_int("42")    # works
convert_to_int("hello") # fails
convert_to_int("100")   # works

# input() always returns a string - you must convert it
def get_user_age():
    while True:         # keep asking until we get a valid inout
        try:
            age = int(input("Enter your age:"))
            if age < 0 or age > 120:
                print("Please enter a realistic age.")
                continue    # skip back to top of loop
            return age
        except ValueError:
            print("That's not a valid number. Please try again.")

age = get_user_age()
print(f"Your age is: {age}")

# WRITING to a file
def write_report(filename, content):
    try:
        with open(filename, 'w') as file:   # 'w' = write mode
            file.write(content)
        print(f"Report saved to {filename}")
    except IOError:
        print(f"Error: Could not write to {filename}")

report_content = """STUDY REPORT
=============
Name    : Juan
Day     : 4
Topic   : Error Handling and File I/O
Status  : Complete
"""

write_report("study_report.txt", report_content)

# READING from a file
def read_report(filename):
    try:
        with open(filename, 'r') as file:   # 'r' = read mode
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: '{filename}' does not exist"

content = read_report("study_report.txt")
print(content)

# Try reading a file that doesn't exist
missing = read_report("does_not_exist.txt")
print(missing)

# APPENDING to a file — 'a' mode adds to the end
def log_activity(filename, activity):
    try:
        with open(filename, 'a') as file:   # 'a' = append mode
            file.write(f"\n{activity}")
        print(f"Logged: {activity}")
    except IOError:
        print("Could not write to log file")

log_activity("study_report.txt", "- Completed file I/O section")
log_activity("study_report.txt", "- Learned try/except/finally")
log_activity("study_report.txt", "- Built error-safe functions")

# Read and print the updated file
print("\n--- Updated Report ---")
print(read_report("study_report.txt"))

