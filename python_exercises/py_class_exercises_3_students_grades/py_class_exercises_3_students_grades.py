import sqlite3
from enum import Enum

# Define an enum for actions
class Actions(Enum):
    ADD_STUDENT = 1
    ADD_GRADE = 2
    VIEW_STUDENTS = 3
    VIEW_GRADES = 4
    UPDATE_STUDENT = 5
    UPDATE_GRADE = 6
    DELETE_STUDENT = 7
    DELETE_GRADE = 8
    EXIT = 9

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('school.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Create the grades table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT NOT NULL,
        grade REAL NOT NULL,
        FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
    )
''')
conn.commit()

# Create Operation for students
def add_student(name):
    cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
    conn.commit()
    print("Student added successfully.")

# Create Operation for grades
def add_grade(student_id, subject, grade):
    cursor.execute("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", (student_id, subject, grade))
    conn.commit()
    print("Grade added successfully.")

# Read Operation for students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Read Operation for grades
def view_grades():
    cursor.execute('''
        SELECT grades.id, students.name, grades.subject, grades.grade
        FROM grades
        JOIN students ON grades.student_id = students.id
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Update Operation for students
def update_student(student_id, name):
    cursor.execute("UPDATE students SET name = ? WHERE id = ?", (name, student_id))
    conn.commit()
    if cursor.rowcount == 0:
        print("Error: Student not found.")
    else:
        print("Student updated successfully.")

# Update Operation for grades
def update_grade(grade_id, subject, grade):
    cursor.execute("UPDATE grades SET subject = ?, grade = ? WHERE id = ?", (subject, grade, grade_id))
    conn.commit()
    if cursor.rowcount == 0:
        print("Error: Grade not found.")
    else:
        print("Grade updated successfully.")

# Delete Operation for students (also deletes related grades)
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Error: Student not found.")
    else:
        print("Student deleted successfully.")

# Delete Operation for grades
def delete_grade(grade_id):
    cursor.execute("DELETE FROM grades WHERE id = ?", (grade_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Error: Grade not found.")
    else:
        print("Grade deleted successfully.")

# Display the menu
def display_menu():
    print("\nMenu:")
    for action in Actions:
        print(f"{action.value}. {action.name.replace('_', ' ').title()}")

# Main function
def main():
    while True:
        display_menu()
        choice = int(input("Please select an option (1-9): "))
        
        if choice == Actions.ADD_STUDENT.value:
            name = input("Enter student name: ")
            add_student(name)
        
        elif choice == Actions.ADD_GRADE.value:
            student_id = int(input("Enter student ID: "))
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            add_grade(student_id, subject, grade)
        
        elif choice == Actions.VIEW_STUDENTS.value:
            view_students()
        
        elif choice == Actions.VIEW_GRADES.value:
            view_grades()
        
        elif choice == Actions.UPDATE_STUDENT.value:
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            update_student(student_id, name)
        
        elif choice == Actions.UPDATE_GRADE.value:
            grade_id = int(input("Enter grade ID to update: "))
            subject = input("Enter new subject: ")
            grade = float(input("Enter new grade: "))
            update_grade(grade_id, subject, grade)
        
        elif choice == Actions.DELETE_STUDENT.value:
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        
        elif choice == Actions.DELETE_GRADE.value:
            grade_id = int(input("Enter grade ID to delete: "))
            delete_grade(grade_id)
        
        elif choice == Actions.EXIT.value:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option, please try again.")

# Run the main function
if __name__ == "__main__":
    main()

# Close the connection when done
conn.close()
