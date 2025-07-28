import numpy as np

# Each row = marks for 1 student in [Math, English, Science]
marks = np.array([
    [75, 80, 72],
    [60, 65, 70],
    [90, 88, 95],
    [55, 58, 60]
])

print("Marks:\n", marks)

# Calculate average mark per student (mean across columns, axis=1)
average_per_student = np.mean(marks, axis=1)

print("\nAverage marks per student:")
for i, avg in enumerate(average_per_student, start=1):
    print(f"Student {i}: {avg:.2f}")

# calculate average mark per subject (mean across rows, axis=0)
average_per_subject = np.mean(marks, axis=0)

subjects = ["Math", "English", "Science"]

print("\nAverage marks per subject:")
for subject, avg in zip(subjects, average_per_subject):
    print(f"{subject}: {avg:.2f}")
