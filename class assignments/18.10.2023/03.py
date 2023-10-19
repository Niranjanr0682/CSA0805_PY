import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a DataFrame
data = pd.read_csv("C://other stuffs//P for Programming//Github//SIMATS//Python project//Private_data.csv")

# Find the student with the highest and lowest scores for management
highest_management_score = data[data['GENERAL MANAGEMENT SCORE (OUT of 50)'] == data[('GENERAL MANAGEMENT SCORE (OUT '
                                                                                      'of 50)')].max()]
lowest_management_score = data[data['GENERAL MANAGEMENT SCORE (OUT of 50)'] == data[('GENERAL MANAGEMENT SCORE (OUT of '
                                                                                     '50)')].min()]

print('Student with the highest management score:')
print(highest_management_score)

print('\nStudent with the lowest management score:')
print(lowest_management_score)

average_scores = data.mean()

plt.bar(['GENERAL MANAGEMENT SCORE (OUT of 50)', 'Domain Specific SCORE (OUT 50)'], [average_scores['GENERAL '
                                                                                                    'MANAGEMENT SCORE'
                                                                                                    ' (OUT of 50)'],
                                                                                     average_scores['Domain Specific '
                                                                                                    'SCORE (OUT 50)']])
plt.xlabel('Achievement Type')
plt.ylabel('Average Score')
plt.title('Average Scores for Management and Domain-specific Achievement')
plt.show()
