# week1_review.py
# Write these from memory - no copy pasting

# 1. A list of technologies you want to learn
technologies = [
    "Python/ Backend Development",
    "SQL (Data Engineer)",
    "Docker(Development)",
    "Machine Learning(AI and Automation)"
]
# 2. A dictionary with your profile (name, age, goal, skills)
profile = {
    "Name" : "Reiko Paulo A. Feckleng",
    "Course" : "Mechatronics Engineering",
    "Goal" : "Software Engineer and Data Engineer"
}
# 3. function that takes a score and returns a grade A-f
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# 4. A for loop that prints each skill form you list
print(" === Technologies I want to learn === ")
for tech in technologies:
    print("-", tech)
# Dispay Profile
print("\n === My Profile ===")
for key, value in profile.items():
    print(f"{key}:{value}")
# 5. A try/except that safely converts user input to a float
print("\n=== Grade Calculator===")
try:
    user_input = input("Enter you score(0-100):")
    score = float(user_input)
    grade = get_grade(score)
    print("Your grade is:", grade)
except ValueError:
    print("Invalid inout! Please enter a number.")
# 6. A class called Developer with name, skills, and an add_skill() method
class Developer:
    def __init__ (self,name):
        self.name = name
        self.skills = []
    
    def add_skill(self, skill):
        self.skills.append(skill)
        
    def show_skills(self):
        print(f"\n{self.name}'s Skills:")
        for skill in self.skills:
            print("-", skill)

# Create a developer object
dev = Developer("Reiko")
dev.add_skill("Python")
dev.add_skill("Git and GitHub")
dev.add_skill("SQL")
dev.add_skill("Docker")
dev.add_skill("Machine Learning")

# Show skill
dev.show_skills()