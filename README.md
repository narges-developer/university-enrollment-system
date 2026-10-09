University Enrollment System

A simple console-based university enrollment system written in Python.

This project allows users to manage student information through a menu-driven interface.

Features
Add a new student
Show all students
Search for a student by student ID
Remove a student by student ID
Exit the program
Data Structure

Each student is stored as a dictionary inside a list:

{
    "name": "Ali",
    "student_id": 1234,
    "major": "Computer Engineering"
}

The program stores multiple students in a list:

students = [
    {
        "name": "Ali",
        "student_id": 1234,
        "major": "Computer Engineering"
    }
]
Concepts Practiced
Variables
Lists
Dictionaries
for loops
while loops
Functions with def
if / elif / else
input()
Type conversion with int()
append()
remove()
Searching through a list of dictionaries
Basic program structure and function decomposition
Menu
1. Add student
2. Show students
3. Search student
4. Remove student
5. Exit
Example
1. Add student
2. Show students
3. Search student
4. Remove student
5. Exit

Enter the number corresponding to your choice: 1

Enter student name: Sara
Enter student ID: 5678
Enter student major: Computer Engineering

Student added successfully.
Project Goal

The main goal of this project was to practice breaking a larger program into smaller functions.

Each function is responsible for one specific task:

add_student() → adds a new student
show_students() → displays all students
search_student() → searches for a student
remove_student() → removes a student
Limitations

This is a beginner-level console application. Student data is stored only while the program is running and is not saved to a file or database.

Future Improvements

Possible improvements for a future version:

Prevent duplicate student IDs
Validate user input
Save student data to a file
Add an update/edit student feature
Improve the user interface
Handle invalid input with try/except
Author

Narges