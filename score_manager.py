# score_manager.py
# Reads scores, handles errors, saves a report to a file

def get_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

def get_score_from_user(subject):
    while True:
        try:
            score = float(input(f"  Enter score for {subject}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("  Score must be between 0 and 100.")
        except ValueError:
            print("  Invalid input. Enter a number.")

def build_report(name, scores):
    lines = []
    lines.append("=" * 45)
    lines.append(f"  STUDENT REPORT — {name.upper()}")
    lines.append("=" * 45)

    total = 0
    for subject, score in scores.items():
        grade = get_grade(score)
        status = "Pass" if score >= 60 else "Fail"
        line = f"  {subject:<18} {score:>5.1f}   {grade}   {status}"
        lines.append(line)
        total += score

    average = total / len(scores)
    lines.append("=" * 45)
    lines.append(f"  Average Score  : {average:.1f} ({get_grade(average)})")
    lines.append("=" * 45)
    return "\n".join(lines)

def save_report(report, filename):
    try:
        with open(filename, 'w') as f:
            f.write(report)
        print(f"\n  Report saved to '{filename}'")
    except IOError:
        print("\n  Warning: Could not save report to file.")

def main():
    print("=" * 45)
    print("   STUDENT SCORE MANAGER")
    print("=" * 45)

    name = input("Enter student name: ").strip()
    if not name:
        name = "Unknown Student"

    subjects = ["Mathematics", "Physics", "Python", "Data Structures"]
    scores = {}

    print(f"\nEnter scores for {name}:")
    for subject in subjects:
        scores[subject] = get_score_from_user(subject)

    report = build_report(name, scores)

    print("\n" + report)

    filename = f"{name.lower().replace(' ', '_')}_report.txt"
    save_report(report, filename)

main()