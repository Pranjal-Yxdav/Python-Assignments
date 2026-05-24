import sqlite3

conn = sqlite3.connect("Assignment5.db")

conn.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT
)
''')

print("Tables created successfully")

conn.execute('insert into students (name, age) values ("Rahul", 20)')
conn.execute('insert into students (name, age) values ("Anita", 21)')

conn.execute('insert into courses (course_name) values ("Python")')
conn.execute('insert into courses (course_name) values ("DBMS")')

conn.commit()
print("Records inserted")

print("\nStudents Table:")
cursor = conn.execute("select * from students")
print(cursor.fetchall())

print("\nCourses Table:")
cursor = conn.execute("select * from courses")
print(cursor.fetchall())

print("\nOnly Student Names:")
cursor = conn.execute("select name from students")
print(cursor.fetchall())

conn.execute('update students set age = 22 where name = "Rahul"')
conn.commit()
print("\nStudent data updated")

conn.execute('delete from courses where course_name = "DBMS"')
conn.commit()
print("Course deleted")

print("\nFinal Students:")
cursor = conn.execute("select * from students")
print(cursor.fetchall())

print("\nFinal Courses:")
cursor = conn.execute("select * from courses")
print(cursor.fetchall())

conn.close()