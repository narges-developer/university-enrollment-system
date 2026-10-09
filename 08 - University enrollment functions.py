# ===========================================
# Project: University Enrollment System
# Description:
# A simple console-based university enrollment
# system for managing student information.
#
# Concepts Used:
# - Variables
# - List
# - Dictionary
# - for loop
# - while loop
# - Functions (def)
# - if / elif / else
# - input
# - int
# - append
# - remove
# ===========================================
students = [
    {
        "name": "Ali",
        "student_id": 1234,
        "major": "Computer Engineering"
    }
]

def add_student():
    new_name = input("Enter student name: ")
    new_id = int(input("Enter student ID: "))
    new_major = input("Enter student major: ")

    students.append({
        "name": new_name,
        "student_id": new_id,
        "major": new_major
    })

    print("Student added successfully.")

def show_students():
    for student in students:
        print("Name:", student["name"])
        print("ID:", student["student_id"])
        print("Major:", student["major"])
        print("----------------")

def search_student():
    student_id = int(input("Enter student ID: "))
    found = False
    for student in students:
        if student_id == student["student_id"]:
            print("Student found!")
            print("Name:", student["name"])
            print("ID:", student["student_id"])
            print("Major:", student["major"])
            found = True
    if not found:
        print("Student not found.")

def remove_student():
    student_id = int(input("Enter student ID: "))
    found = False
    for student in students:
        if student_id == student["student_id"]:
            students.remove(student)
            found = True
            print("Student removed successfully.")
            break
    if not found:
        print("Student not found.")

menu = [
    "1. Add student",
    "2. Show students",
    "3. Search student",
    "4. Remove student",
    "5. Exit"
]

while True:
    for item in menu:
        print(item)
    user_selection = int(input("Enter the number corresponding to your choice: "))
    if user_selection == 1:
        add_student()
        print("-----------------------")
    elif user_selection == 2:
        show_students()
        print("-----------------------")
    elif user_selection == 3:
        search_student()
        print("-----------------------")
    elif user_selection == 4:
        remove_student()
        print("-----------------------")
    elif user_selection == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")