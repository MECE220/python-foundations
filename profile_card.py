# profile_card.py
# My professional profile card

def print_separator():
    print("-" * 40)

def display_profile(profile):
    print_separator()
    print(f" Name  : {profile['name']}")
    print(f" Age   : {profile['age']}")
    print(f" Degree: {profile['degree']}")
    print(f" Goal  : {profile['goal']}")
    print_separator()
    print("SKILLS:")
    for skill in profile['skills']:
        print(f" - {skill}")
    print_separator()

# Your data
my_profile = {
    "name": "Reiko Paulo A. Feckleng",
    "age": 25,
    "degree": "Mechatronics Engineer",
    "goal": "Software/Data/AI Engineer at Oracle",
    "skills": ["Python", "Git", "Linux", "Problem Solving", "SQL", "Docker"]
}

display_profile(my_profile)