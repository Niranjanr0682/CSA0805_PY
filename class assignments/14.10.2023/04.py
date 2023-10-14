# Given a list of tuples, each containing a student's name and their scores in three
# subjects, calculate and display the average score for each student. Store the results
# in a dictionary with student names as keys and average scores as values.

def calculate_average_scores(student_scores):
    average_scores = {}
    for student in student_scores:
        name, scores = student[0], student[1:]
        average = sum(scores) / len(scores)
        average_scores[name] = average
    return average_scores


def get_student_scores():
    student_scores = []
    while True:
        name = input("Enter student name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        scores = []
        for i in range(3):
            score = int(input(f"Enter score for subject {i + 1}: "))
            scores.append(score)
        student_scores.append((name, *scores))
    return student_scores


student_scores = get_student_scores()
average_scores_dict = calculate_average_scores(student_scores)
for student, average in average_scores_dict.items():
    print(f"{student}: Average Score = {average:.2f}")
