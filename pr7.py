import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="240760107016"
)
cursor = connection.cursor()
print("Connected to MySQL successfully!")

sql = "INSERT INTO students (id, name, year, sem) VALUES (%s, %s, %s, %s)"
values = [
    (1, "Ayan", "3rd", 5),
    (2, "Harsh", "2nd", 4)
]
cursor.executemany(sql, values)
connection.commit()
print("Students inserted successfully.")

print("\nStudent Records:")
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
for student in students:
    print(student)

sql_update = "UPDATE students SET name=%s, year=%s, sem=%s WHERE id=%s"
val_update = ("Dharmik", "3rd", 5, 2)
cursor.execute(sql_update, val_update)
connection.commit()
print("\nStudent updated successfully.")

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
for student in students:
    print(student)

sql_delete = "DELETE FROM students WHERE id=%s"
cursor.execute(sql_delete, (2,))
connection.commit()
print("\nStudent deleted successfully.")

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
for student in students:
    print(student)

cursor.close()
connection.close()