# grade_analyzer.py
# Analyzes a list of scores and produces a report

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

def analyze_scores(subject_scores):
    print("=" * 45)
    print("GRADE REPORT")
    print("=" * 45)
    
    total = 0
    highest = 0
    lowest = 100
    passed = 0
    
    for subject, score in subject_scores.items():
        grade = get_grade(score)
        
        # track stats
        total += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
        if score >= 60:
            passed += 1
        
        # print each subject
        status = "✔️ Pass" if score >= 60 else "❌ Fail"
        print(f" {subject:<20} {score:>3} {grade} {status}")
              
    print("=" * 45)
    
    average = total / len(subject_scores)
    overall_grade = get_grade(average)
    
    print(f" Average Score : {average:.1f} ({overall_grade})")
    print(f" Highest Score   : {highest}")
    print(f" Lowest Score    : {lowest}")
    print(f" Subjects Passed : {passed}/{len(subject_scores)}")
    print("=" * 45)
    
# Your scores - change these to whatever you like
my_scores = {
    "Mathematics"     : 95,
    "Physics"         : 88,
    "Python Basics"   : 92,
    "Data Structures" : 85,
    "Thermodynamics"  : 80,
}

analyze_scores(my_scores)