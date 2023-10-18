# Use the data from csv file (previous lesson) to create a bar chart using Matplotlib to
# visualize any data of your choice. Ensure that the chart is clear and visually appealing
# (color, label and title).

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('C://other stuffs//P for Programming//Github//SIMATS//Python project//data.csv')
df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

plt.bar(X, Y, color='g')
plt.title("Students over 11 Years")
plt.xlabel("Years")
plt.ylabel("Number of Students")
plt.show()
