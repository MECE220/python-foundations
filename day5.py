# day5.py
# Without OOP - scattered data and functions
name1 = "Reiko"
age1 = 25
degree1 = "Mechatronics Engineering"

name2 = "Yuki"
age2 = 24
degree2 = "Computer Science"

#def introduce(name, age, degree):
 #   print(f"Hello, my name is {name}, {age} years old, {degree} graduate.")
    
#introduce(name1, age1, degree1)
#introduce(name2, age2, degree2)

# With OOP - data and functions bundled together in a class
class Student:
    
    def __init__(self, name, age, degree):  # constructor
        self.name = name     # attribute
        self.age = age       # attribute
        self.degree = degree # attribute
        
    def introduce(self): # method
        print(f"Hi, I'm {self.name}, {self.age} years old, {self.degree} graduate.")

# Create object from the class
student1 = Student("Reiko", 25, "Mechatronics Engineering")
student2 = Student("Yuki", 24, "Computer Science")

# Access attributes directly
print(student1.name) # Reiko
print(student1.degree)

# PART 2 — Methods: Functions That Belong to Objects

class Student:
    
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
        self.grades = {}    # starts as empty dictionary
        self.is_enrolled = True
    
    def introduce(self):
        status = "enrolled" if self.is_enrolled else "not enrolled"
        print(f"Hi, I am {self.name}, {self.degree} graduate - currently {status}.")
    
    def add_grade(self, subject, score):
        self.grades[subject] = score
        print(f" Added: {subject} = {score}")
    
    def get_average(self):
        if not self.grades:         # if grades dictionary is empty
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)
    
    def show_report(self):
        print(f"\n--- Report for {self.name} ---")
        for subject, score in self.grades.items():
            print(f" {subject}: {score}")
        print(f" Average: {self.get_average():.1f}")
        
# Create student and use their methods
reiko = Student("Reiko", 25, "Mechatronics Engineering")
reiko.introduce()

reiko.add_grade("Python", 95)
reiko.add_grade("Math", 88)
reiko.add_grade("Physics", 92)

reiko.show_report()

# PART 3 — Inheritance: Reusing and Extending Classes 

# Parent class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age} years old.")


# Child class — inherits from Person
class Engineer(Person):

    def __init__(self, name, age, specialization, company=None):
        super().__init__(name, age)   # call parent constructor
        self.specialization = specialization
        self.company = company
        self.skills = []

    def introduce(self):              # override parent method
        super().introduce()           # still call parent version
        print(f"I am a {self.specialization} Engineer at {self.company or 'currently job hunting'}.")

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"  Skill added: {skill}")

    def show_skills(self):
        print(f"\n{self.name}'s skills:")
        for skill in self.skills:
            print(f"  - {skill}")


# Another child class
class DataEngineer(Engineer):

    def __init__(self, name, age, company=None):
        super().__init__(name, age, "Data", company)
        self.pipelines = []

    def add_pipeline(self, pipeline_name):
        self.pipelines.append(pipeline_name)
        print(f"  Pipeline built: {pipeline_name}")

    def show_portfolio(self):
        print(f"\n{self.name}'s Data Engineering Portfolio:")
        for p in self.pipelines:
            print(f"  - {p}")


# Use all three classes
person = Person("Alice", 30)
person.introduce()

engineer = Engineer("Reiko", 28, "Software", "Google")
engineer.introduce()
engineer.add_skill("Python")
engineer.add_skill("Java")
engineer.show_skills()

# This is YOU in 12 months
future_you = DataEngineer("Reiko", 25, "Oracle")
future_you.introduce()
future_you.add_skill("Python")
future_you.add_skill("SQL")
future_you.add_skill("Apache Spark")
future_you.add_skill("Java")
future_you.add_pipeline("Real-Time Sales ETL Pipeline")
future_you.add_pipeline("AI-Powered Analytics Platform")
future_you.show_skills()
future_you.show_portfolio()
future_you.birthday()   # inherited from Person!

# PART 4 — Encapsulation: Protecting Your Data

class BankAccount:
    
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance    # __ makes it private
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" Deposit: ${amount:.2f}")
        else:
            print(" Error:Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if amount <= 0:
            print(" Error: Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print(f" Error: Insufficient funds. Balance: ${self.__balance:.2f}")
        else:
            self.__balance -= amount
            print(f" Withdrawn: ${amount:.2f}")
    
    def get_balance(self):
        return self.__balance
    
    def show_statement(self):
        print(f"\n Account owner : {self.owner}")
        print(f" Balance : ${self.get_balance():.2f}")
        
# Use the Bank account
account = BankAccount("Reiko", 1000)
account.show_statement()

account.deposit(500)
account.withdraw(200)
account.withdraw(2000) # should fail - insufficient funds
account.deposit(-50)   # should fail - negative amount

account.show_statement()

# Try to access private attribute directly - this will fail
try:
    print(account.__balance)
except AttributeError:
    print("\n Cannot access __balance directly - it's private!")