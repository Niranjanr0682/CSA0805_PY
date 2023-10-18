# Write a program that reads a dataset containing information on diamonds (previous
# lesson db file). Utilize a any visualization library of your choice to create a scatter
# plot.

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect("C://other stuffs//P for Programming//Github//SIMATS//Python project//mydb.db")
query = "SELECT * FROM 'diamonds' LIMIT 0,30"
data = pd.read_sql_query(query, connection)

connection.close()
plt.figure(figsize=(10, 6))
plt.scatter(data["carat"], data["price"], alpha=0.5)  # alpha controls point transparency
plt.xlabel("Carat")
plt.ylabel("Price")
plt.title("Scatter Plot of Diamonds - Carat vs. Price")
plt.show()







