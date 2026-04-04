# ============================================
# Assignment Part 1: Student Grade Tracker
# ============================================

# -------------------------------
# Task 1: Data Parsing & Cleaning
# -------------------------------

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    # Clean name
    name = student["name"].strip().title()

    # Validate name (only alphabetic words)
    is_valid_name = all(word.isalpha() for word in name.split())

    # Convert roll to integer
    roll = int(student["roll"])

    # Convert marks string to list of integers
    marks = [int(m) for m in student["marks_str"].split(", ")]

    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    # Print validation result
    if is_valid_name:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")

    # Print formatted profile card
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)

# Print ALL CAPS and lowercase name for roll number 103
for student in cleaned_students:
    if student["roll"] == 103:
        print(student["name"].upper())
        print(student["name"].lower())

# ----------------------------------------
# Task 2: Marks Analysis & User Interaction
# ----------------------------------------

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("\nSubject-wise Report:")

for subject, mark in zip(subjects, marks):
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subject}: {mark} ({grade})")

total_marks = sum(marks)
average_marks = round(total_marks / len(marks), 2)

highest_index = marks.index(max(marks))
lowest_index = marks.index(min(marks))

print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Scoring Subject:", subjects[highest_index], "-", marks[highest_index])
print("Lowest Scoring Subject:", subjects[lowest_index], "-", marks[lowest_index])

# While loop for marks entry
new_subjects = 0

while True:
    subject = input("\nEnter subject name (or 'done' to finish): ").strip()

    if subject.lower() == "done":
        break

    try:
        score = float(input("Enter marks (0–100): "))
        if 0 <= score <= 100:
            subjects.append(subject)
            marks.append(score)
            new_subjects += 1
        else:
            print("Invalid marks! Must be between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a number.")

updated_average = round(sum(marks) / len(marks), 2)

print("\nNew subjects added:", new_subjects)
print("Updated Average:", updated_average)

# --------------------------------------
# Task 3: Class Performance Summary
# --------------------------------------

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\nName              | Average | Status")
print("-" * 40)

pass_count = 0
fail_count = 0
averages = {}

for name, marks_list in class_data:
    avg = round(sum(marks_list) / len(marks_list), 2)
    status = "Pass" if avg >= 60 else "Fail"

    averages[name] = avg

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    print(f"{name:<18} |  {avg:<6} | {status}")

topper = max(averages, key=averages.get)
class_average = round(sum(averages.values()) / len(averages), 2)

print("\nPassed:", pass_count)
print("Failed:", fail_count)
print("Class Topper:", topper, "-", averages[topper])
print("Class Average:", class_average)

# --------------------------------------
# Task 4: String Manipulation Utility
# --------------------------------------

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1
clean_essay = essay.strip().lower()
print("\nClean Essay:", clean_essay)

# Step 2
print("\nTitle Case:", clean_essay.title())

# Step 3
python_count = clean_essay.count("python")
print("\nCount of 'python':", python_count)

# Step 4
replaced_essay = clean_essay.replace("python", "Python 🐍")
print("\nReplaced Essay:", replaced_essay)

# Step 5
sentences = clean_essay.split(". ")
print("\nSentences List:", sentences)

# Step 6
print("\nNumbered Sentences:")
for i, sentence in enumerate(sentences, 1):
    sentence = sentence.strip()
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")