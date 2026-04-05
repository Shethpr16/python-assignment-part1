# ============================================
# Part 1: Student Grade Tracker
# Demonstrates Python basics, loops, conditionals,
# string manipulation, and list/dictionary handling
# ============================================


# -------------------------------
# Task 1: Data Parsing & Cleaning
# -------------------------------

# Raw student data (uncleaned)
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# This list will store cleaned student data
cleaned_students = []

# Loop through each student dictionary
for student in raw_students:
    
    # Remove extra spaces and convert name to Title Case
    name = student["name"].strip().title()
    
    # Convert roll number from string to integer
    roll = int(student["roll"])
    
    # Convert marks string into a list of integers
    marks = [int(m) for m in student["marks_str"].split(", ")]

    # Validate name: each word must contain only alphabets
    is_valid_name = True
    for word in name.split():
        if not word.isalpha():
            is_valid_name = False

    # Print name validation result
    if is_valid_name:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")

    # Store cleaned data in a new list
    cleaned_students.append({
        "name": name,
        "roll": roll,
        "marks": marks
    })

    # Print formatted student profile card
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)


# Print ALL CAPS and lowercase versions of name for roll number 103
for student in cleaned_students:
    if student["roll"] == 103:
        print(student["name"].upper())
        print(student["name"].lower())


# ----------------------------------------
# Task 2: Marks Analysis (Loops & Conditions)
# ----------------------------------------

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("\n--- Subject-wise Performance ---")

# Loop through subjects and marks together
for i in range(len(subjects)):
    subject = subjects[i]
    mark = marks[i]

    # Determine grade based on marks
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

    print(f"{subject}: {mark} → Grade {grade}")

# Calculate total and average marks
total_marks = sum(marks)
average_marks = round(total_marks / len(marks), 2)

print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)

# Identify highest and lowest scoring subjects
highest_index = marks.index(max(marks))
lowest_index = marks.index(min(marks))

print("Highest Scoring Subject:", subjects[highest_index], "-", marks[highest_index])
print("Lowest Scoring Subject:", subjects[lowest_index], "-", marks[lowest_index])


# ----------------------------------------
# Task 3: Class Performance Summary
# ----------------------------------------

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
student_averages = {}

# Loop through class data
for name, mark_list in class_data:
    avg = round(sum(mark_list) / len(mark_list), 2)
    
    # Determine pass or fail status
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    student_averages[name] = avg
    print(f"{name:<18} |  {avg:<6} | {status}")

# Identify topper and class average
topper = max(student_averages, key=student_averages.get)
class_average = round(sum(student_averages.values()) / len(student_averages), 2)

print("\nPassed:", pass_count)
print("Failed:", fail_count)
print("Class Topper:", topper, "-", student_averages[topper])
print("Class Average:", class_average)


# ----------------------------------------
