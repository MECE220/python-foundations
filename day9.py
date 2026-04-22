# day9.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NUMPY ARRAYS - like Python lists but 100x faster for math
scores = np.array([88, 95, 72, 65, 91, 78, 84, 69, 93, 76])
print("Array:", scores)
print("Type:", type(scores))

# Math on entire array at once - no loop needed
print("\n--- Array math ---")
print("Mean:    ", np.mean(scores))    # average
print("Median:  ", np.std(scores))    # middle value
print("Std:     ", np.std(scores).round(2))     # spread
print("Min:     ", np.min(scores))
print("Max:     ", np.max(scores))
print("Sum:     ", np.sum(scores))

# Operations apply to ALL elements instantly
print("\n--- Element-wise operations ---")
print("Scores + 5:      ", scores + 5)
print("Scores * 2:      ", scores * 2)
print("Scores above 80:     ", scores[scores > 80])   # filter!
print("How many > 80:        ", np.sum(scores > 80))  

# NUMPY RANGES AND SHAPES
print("\n--- Creating arrays ---")
zeros = np.zeros(5)              # [0. 0. 0. 0. 0.]
ones = np.ones(5)                # [1. 1. 1. 1. 1.]
sequence = np.arange(0, 10, 2)  # [0 2 4 6 8]
random = np.random.randint(60, 100, size=10)  # 10 random scores

print("Zeros:   ", zeros)
print("Ones:    ", ones)
print("Sequence:", sequence)
print("Random:  ", random)

# 2D ARRAY — rows and columns (like a mini DataFrame)
grades_2d = np.array([
    [88, 92, 75],    # student 1: math, science, english
    [95, 88, 91],    # student 2
    [72, 65, 80],    # student 3
    [65, 70, 68]     # student 4
])

print("\n--- 2D Array ---")
print(grades_2d)
print("Shape:", grades_2d.shape)          # (4, 3) = 4 rows, 3 cols
print("Row 0:", grades_2d[0])             # first student's grades
print("Col 0:", grades_2d[:, 0])          # all students' math scores
print("Average per student:", np.mean(grades_2d, axis=1).round(1))
print("Average per subject:", np.mean(grades_2d, axis=0).round(1))

# Set up data for all charts
subjects = ["Math", "Science", "English", "Python", "History"]
scores_data = [88, 92, 75, 95, 70]
students = ["Reiko", "Maria", "Pedro", "Juan", "Ana"]
student_scores = [88, 95, 72, 65, 91]
monthly_scores = [65, 70, 72, 78, 82, 85, 88, 91, 93, 95, 97, 99]
months = ["Juan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

plt.figure(figsize=(8, 5))
bars = plt.bar(subjects, scores_data, color=["#4C72B0","#DD8452","#55A868","#C44E52","#8172B2"])
plt.title("Scores by Subject", fontsize=14, fontweight="bold")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.ylim(0, 100)

# Add value labels on top of bars
for bar, score in zip(bars, scores_data):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(score), ha="center", fontsize=10)

plt.tight_layout()
plt.savefig("chart_bar.png")
plt.close()
print("Saved: chart_bar.png")

plt.figure(figsize=(10, 5))
plt.plot(months, monthly_scores, marker="o", color="#4C72B0",
         linewidth=2, markersize=6)
plt.fill_between(months, monthly_scores, alpha=0.1, color="#4C72B0")
plt.title("Learning Progress Over 12 Months", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Score")
plt.ylim(50, 105)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart_line.png")
plt.close()
print("Saved: chart_line.png")

plt.figure(figsize=(8, 5))
colors = ["#55A868" if s >= 80 else "#C44E52" for s in student_scores]
plt.barh(students, student_scores, color=colors)
plt.title("Student Scores (Green = Pass, Red = Fail)", fontsize=14, fontweight="bold")
plt.xlabel("Score")
plt.xlim(0, 100)
plt.axvline(x=60, color="gray", linestyle="--", alpha=0.7, label="Pass line")
plt.legend()
plt.tight_layout()
plt.savefig("chart_horizontal.png")
plt.close()
print("Saved: chart_horizontal.png")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Data Analysis Dashboard", fontsize=16, fontweight="bold")

# Top left — bar
axes[0, 0].bar(subjects, scores_data, color="#4C72B0")
axes[0, 0].set_title("Scores by Subject")
axes[0, 0].set_ylim(0, 100)

# Top right — line
axes[0, 1].plot(months, monthly_scores, marker="o", color="#DD8452")
axes[0, 1].set_title("Progress Over Time")
axes[0, 1].tick_params(axis="x", rotation=45)

# Bottom left — horizontal bar
axes[1, 0].barh(students, student_scores, color="#55A868")
axes[1, 0].set_title("Student Comparison")

# Bottom right — pie chart
pass_fail = [sum(1 for s in student_scores if s >= 60),
             sum(1 for s in student_scores if s < 60)]
axes[1, 1].pie(pass_fail, labels=["Pass", "Fail"],
               colors=["#55A868", "#C44E52"],
               autopct="%1.0f%%", startangle=90)
axes[1, 1].set_title("Pass/Fail Rate")

plt.tight_layout()
plt.savefig("dashboard.png")
plt.close()
print("Saved: dashboard.png")