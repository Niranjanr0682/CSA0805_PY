# Create a dictionary of student names and a corresponding tuple of their exam
# scores. Write a program to find and display the name of the student with the highest
# score.

student_scores = {
    "niranjan": (95, 85, 90),
    "sridev": (80, 90, 85),
    "dinesh": (90, 95, 92),
    "Deva": (85, 80, 95),
    "santhosh": (92, 90, 93),
}
highest_score = 0
student_with_highest_score = ""
for student, scores in student_scores.items():
    total_score = sum(scores)
    if total_score > highest_score:
        highest_score = total_score
        student_with_highest_score = student
print(f"The student with the highest score is {student_with_highest_score}.")


