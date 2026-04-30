# student_system.py
# A complete OOP-based student management system

class Student:

    student_count = 0   # class variable — shared across ALL students

    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree
        self.__grades = {}
        Student.student_count += 1
        self.student_id = f"STU{Student.student_count:03d}"

    def add_grade(self, subject, score):
        try:
            score = float(score)
            if 0 <= score <= 100:
                self.__grades[subject] = score
            else:
                print(f"  Error: Score must be 0-100")
        except ValueError:
            print(f"  Error: Invalid score")

    def get_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values()) / len(self.__grades)

    def get_grade_letter(self, score):
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "F"

    def show_report(self):
        print(f"\n{'='*45}")
        print(f"  Student  : {self.name} ({self.student_id})")
        print(f"  Age      : {self.age}")
        print(f"  Degree   : {self.degree}")
        print(f"{'='*45}")
        if self.__grades:
            for subject, score in self.__grades.items():
                grade = self.get_grade_letter(score)
                print(f"  {subject:<20} {score:>5.1f}   {grade}")
            print(f"{'='*45}")
            avg = self.get_average()
            print(f"  Average  : {avg:.1f} ({self.get_grade_letter(avg)})")
        else:
            print("  No grades recorded yet.")
        print(f"{'='*45}")

    def __str__(self):    # special method — defines print(student)
        return f"Student({self.student_id}: {self.name}, {self.degree})"


class Classroom:

    def __init__(self, course_name):
        self.course_name = course_name
        self.__students = []

    def enroll(self, student):
        self.__students.append(student)
        print(f"  Enrolled: {student.name} → {self.course_name}")

    def show_all_students(self):
        print(f"\n{'='*45}")
        print(f"  COURSE: {self.course_name}")
        print(f"  Total Students: {len(self.__students)}")
        print(f"{'='*45}")
        for student in self.__students:
            avg = student.get_average()
            print(f"  {student.name:<20} Avg: {avg:.1f}")
        print(f"{'='*45}")

    def get_top_student(self):
        if not self.__students:
            return None
        return max(self.__students, key=lambda s: s.get_average())


# --- Main Program ---
print("="*45)
print("   STUDENT MANAGEMENT SYSTEM")
print("="*45)

# Create students
reiko = Student("Reiko", 23, "Mechatronics")
maria = Student("Maria", 22, "Computer Science")
pedro = Student("Pedro", 24, "Electrical Engineering")

# Add grades
reiko.add_grade("Python", 95)
reiko.add_grade("Mathematics", 88)
reiko.add_grade("Data Structures", 91)

maria.add_grade("Python", 98)
maria.add_grade("Mathematics", 85)
maria.add_grade("Data Structures", 94)

pedro.add_grade("Python", 82)
pedro.add_grade("Mathematics", 79)
pedro.add_grade("Data Structures", 87)

# Show individual reports
reiko.show_report()
maria.show_report()

# Create a classroom and enroll students
cs101 = Classroom("Introduction to Programming")
cs101.enroll(reiko)
cs101.enroll(maria)
cs101.enroll(pedro)

cs101.show_all_students()

# Find top student
top = cs101.get_top_student()
print(f"\n  Top Student: {top.name} with average {top.get_average():.1f}")

# Test __str__ method
print(f"\n  {reiko}")
print(f"  Total students created: {Student.student_count}")