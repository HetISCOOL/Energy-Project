import pandas as pd
import sqlite3

# Load the CSV
df = pd.read_csv(r"C:\Users\naine\OneDrive\Desktop\New folder\iou_zipcodes_2020.csv")

# Connect to a SQLite database (or create one)
try:
    conn = sqlite3.connect('energy.db')
    
    # Convert CSV to SQLite table
    df.to_sql('table_name', conn, if_exists='replace', index=False)
    print("Data successfully loaded into the database.")
    
except Exception as e:
    print("An error occurred:", e)
    
finally:
    # Close the connection
    conn.close()
