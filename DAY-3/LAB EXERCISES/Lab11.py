import mysql.connector
import pandas as pd

# Establish connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Root@123',
    database='dblab11'
)

# Query to fetch data from the DBMS
query = "SELECT * FROM Sales"

# Read the data into a pandas DataFrame
df = pd.read_sql(query, conn)

print(df)


df.to_excel('output_data.xlsx', index=False, engine='openpyxl')

# Close the connection
conn.close()
