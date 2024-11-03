import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect(r"C:\Users\naine\OneDrive\Desktop\Energy Project\energy.db")

# SQL query to calculate average rates per state
query = """
    SELECT state, 
        AVG(comm_rate) AS avg_comm_rate, 
        AVG(ind_rate) AS avg_ind_rate, 
        AVG(res_rate) AS avg_res_rate
    FROM table_name
    GROUP BY state
    order by avg_comm_rate, avg_ind_rate, avg_res_rate desc
    limit 10
"""

# Load the query result into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# 1. Descriptive Statistics
print("Descriptive Statistics:")
print(df[['avg_comm_rate', 'avg_ind_rate', 'avg_res_rate']].describe())

# Plotting the data -- BAR GRAPH
# Set up the figure for the plot with a specific size
plt.figure(figsize=(12, 8))

# Plot average commercial, industrial, and residential rates for each state
bar_width = 0.25
x = range(len(df['state']))

# Plot each rate as a separate bar, offset by width
plt.bar(x, df['avg_comm_rate'], width=bar_width, color='#2eb8b8', label='Commercial Rate')
plt.bar([p + bar_width for p in x], df['avg_ind_rate'], color='#85e0e0', width=bar_width, label='Industrial Rate')
plt.bar([p + bar_width*2 for p in x], df['avg_res_rate'], color='#c2f0f0' , width=bar_width, label='Residential Rate')

# Set the title of the plot
plt.title("Average Electricity Rates by State")

# Label the x-axis as "State" and y-axis as "Average Rate"
plt.xlabel("State")
plt.ylabel("Average Rate")

# Set the x-ticks to be the states
plt.xticks([p + bar_width for p in x], df['state'])

# Add a legend to differentiate the types of rates
plt.legend()

# Adjust the layout to ensure everything fits within the figure area
plt.tight_layout()

# Display the plot
plt.show()