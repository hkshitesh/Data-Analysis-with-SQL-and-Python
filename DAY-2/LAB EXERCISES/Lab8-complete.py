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


# Step 4: Update multiple records
update_query = "UPDATE students SET age = %s WHERE id = %s"
update_data = [
    (21, 1),  # Update Alice's age
    (23, 2)   # Update Bob's age
]
cursor.executemany(update_query, update_data)
conn.commit()
print(cursor.rowcount, "rows updated.")

cursor.execute("SELECT * FROM students")
rows= cursor.fetchall()
for row in rows:
    print(row)

# Step 5: Delete records
delete_query = "DELETE FROM students WHERE id = %s"
delete_data = [
    (3,),  # Delete Charlie
]
cursor.executemany(delete_query, delete_data)
conn.commit()
print(cursor.rowcount, "row(s) deleted.")

# Step 6: Display remaining records
cursor.execute("SELECT * FROM students")
print("\nRemaining records:")
for row in cursor.fetchall():
    print(row)

# Step 7: Close connection
cursor.close()
conn.close()

