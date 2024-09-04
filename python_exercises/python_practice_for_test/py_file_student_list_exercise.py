from py_file_manipulation import writeOnFile, appendToFile
from enum import Enum
import json

Students = []

class Actions(Enum):
    ADD_STUDENT = 1
    SHOW_STUDENT = 2
    SHOW_ALL_STUDENTS = 3
    SHOW_DELETED_STUDENTS = 4
    UPDATE_STUDENT = 5
    DELETE_STUDENT = 6
    EXIT = 7

def AddStudent(Name, Email):
    StudentID = len(Students) + 1

    # By default, new students are not hidden
    Hidden = 0

    NewStudent = {
        "StudentID": StudentID,
        "Name": Name,
        "Email": Email,
        "Hidden": Hidden
    }

    Students.append(NewStudent)
    print(f"Student {Name} added to the list.")

def ShowStudent(StudentID):
    Found = False
    for Student in Students:
        if Student["StudentID"] == StudentID:
            print(f"ID: {Student['StudentID']}, Name: {Student['Name']}, Email: {Student['Email']}, Hidden: {Student['Hidden']}")
            Found = True
            break
    if not Found:
        print("Student ID not found.")

def ShowAllStudents(Hidden=0):
    HiddenBoolean = bool(Hidden)

    if not Students:
        print("No students available.")
    else:
        print("Students:")
        for Student in Students:
            IsHidden = bool(Student["Hidden"])
            if not IsHidden or HiddenBoolean:
                print(f"ID: {Student['StudentID']}, Name: {Student['Name']}, Email: {Student['Email']}")

def ShowDeletedStudents():
    if not Students:
        print("No students available.")
    else:
        print("Deleted Students:")
        for Student in Students:
            if Student["Hidden"] == 1:
                print(f"ID: {Student['StudentID']}, Name: {Student['Name']}, Email: {Student['Email']}")

def UpdateStudent(StudentID, Name=None, Email=None):
    Updated = False
    for Student in Students:
        if Student["StudentID"] == StudentID:
            if Name is not None:
                Student["Name"] = Name
            if Email is not None:
                Student["Email"] = Email
            print(f"Student ID {StudentID} has been updated.")
            Updated = True
            break
    if not Updated:
        print("Student ID not found.")

def Menu():
    print("Menu:")
    for Option in Actions:
        print(f"{Option.value}: {Option.name}")

def HandleChoice(Choice):
    if Choice == Actions.ADD_STUDENT:
        print("You selected: Add Student")
        Name = input("Enter student's name: ")
        Email = input("Enter student's email: ")
        AddStudent(Name, Email)
    elif Choice == Actions.SHOW_STUDENT:
        print("You selected: Show Student")
        StudentIDInput = input("Enter the student ID to display: ").strip()
        StudentID = int(StudentIDInput) if StudentIDInput.isdigit() else None
        if StudentID:
            ShowStudent(StudentID)
    elif Choice == Actions.SHOW_ALL_STUDENTS:
        print("You selected: Show All Students")
        ShowAllStudents(Hidden=0)  # Default to not showing hidden students
    elif Choice == Actions.SHOW_DELETED_STUDENTS:
        print("You selected: Show Deleted Students")
        ShowDeletedStudents()
    elif Choice == Actions.UPDATE_STUDENT:
        print("You selected: Update Student")
        StudentIDInput = input("Enter the student ID to update: ").strip()
        StudentID = int(StudentIDInput) if StudentIDInput.isdigit() else None
        if StudentID:
            Name = input("Enter new name (or leave blank to keep current): ").strip() or None
            Email = input("Enter new email (or leave blank to keep current): ").strip() or None
            UpdateStudent(StudentID, Name, Email)
    elif Choice == Actions.DELETE_STUDENT:
        print("You selected: Delete Student")
        StudentIDInput = input("Enter the student ID to delete: ").strip()
        StudentID = int(StudentIDInput) if StudentIDInput.isdigit() else None
        if StudentID:
            for Student in Students:
                if Student["StudentID"] == StudentID:
                    Student["Hidden"] = 1  # Mark student as hidden
                    print(f"Student ID {StudentID} is now marked as hidden.")
                    break
            else:
                print("Student ID not found.")
    elif Choice == Actions.EXIT:
        print("You selected Exit")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def Main():
    while True:
        Menu()
        try:
            UserInput = int(input("Enter your choice: "))
            Choice = Actions(UserInput)
            if not HandleChoice(Choice):
                break
        except (ValueError, KeyError):
            print("Invalid input. Please enter a number from the menu.")

if __name__ == "__main__":
    Main()
