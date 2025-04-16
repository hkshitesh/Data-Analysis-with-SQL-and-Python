import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="PythonDB"
)
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        age INT
    )
""")

# Insert multiple records using executemany()
insert_query = "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)"
students_data = [
    (1, 'Alice', 20),
    (2, 'Bob', 22),
    (3, 'Charlie', 21)
]

cursor.executemany(insert_query, students_data)
conn.commit()

print(cursor.rowcount, "rows inserted.")

# Fetch to verify
cursor.execute("SELECT * FROM students")
rows= cursor.fetchall()
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()
