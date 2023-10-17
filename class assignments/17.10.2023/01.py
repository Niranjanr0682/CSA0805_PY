import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv('C://other stuffs//P for Programming//Github//SIMATS//Python project//data.csv')
# Assuming your CSV has columns 'Category' and 'Value'
categories = data['PlacementStatus']
values = data['CGPA']

# Plotting the bar chart
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.bar( values,categories, color=['skyblue','black'])

# Adding labels and title
plt.ylabel('Categories')
plt.xlabel('Values')
plt.title('Bar Chart of Values by Categories')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
