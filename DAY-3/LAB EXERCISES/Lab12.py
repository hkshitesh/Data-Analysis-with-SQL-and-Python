import mysql.connector
import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('input_data.xlsx', engine='openpyxl')


# Establish connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Root@123',
    database='dblab11'
)

# Create a cursor object
cursor = conn.cursor()

# SQL Query to insert data into the table
insert_query = """
    INSERT INTO user (id, name, age, sal) 
    VALUES (%s, %s, %s, %s)
"""

# Insert rows from the DataFrame into the MySQL table
for i, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

# Commit the transaction
conn.commit()
print("Data imported successfully")
# Close the connection
cursor.close()
conn.close()
