🎓 University Enrollment System

A simple console-based university enrollment system built with Python.

This project was created to practice organizing a larger program into small, reusable functions while working with lists and dictionaries.

✨ Features
Feature	Description
➕ Add Student	Add a new student with name, ID, and major
👥 Show Students	Display all registered students
🔍 Search Student	Find a student by student ID
🗑️ Remove Student	Remove a student using their ID
🚪 Exit	Close the application
🖥️ Menu
1. Add student
2. Show students
3. Search student
4. Remove student
5. Exit
🧠 Concepts Practiced

This project focuses on the following Python concepts:

Functions (def)
Lists
Dictionaries
for loops
while loops
if / elif / else
User input
Type conversion with int()
append()
remove()
Searching through a list of dictionaries
Breaking a program into multiple functions
🗂️ Data Structure

Each student is represented using a dictionary:

{
    "name": "Ali",
    "student_id": 1234,
    "major": "Computer Engineering"
}

Multiple students are stored inside a list:

students = [
    {
        "name": "Ali",
        "student_id": 1234,
        "major": "Computer Engineering"
    }
]
⚙️ How It Works

The program is divided into four main functions:

add_student()
      ↓
Adds a new student

show_students()
      ↓
Displays all students

search_student()
      ↓
Searches by student ID

remove_student()
      ↓
Removes a student by ID

A while loop controls the main menu and allows the user to perform multiple operations until choosing Exit.

▶️ How to Run

Make sure Python is installed, then run:

python "08 - University enrollment functions.py"
🚀 Future Improvements

Possible improvements for future versions:

Prevent duplicate student IDs

Validate user input

Handle invalid inputs with try/except

Add an Update Student feature

Save student data to a file

Load existing data when the program starts

Improve the console interface

📚 Project Purpose

The main goal of this project was to practice function decomposition — taking a relatively larger program and dividing it into smaller functions, with each function responsible for one specific task.

This project is part of my ongoing Python programming practice and portfolio development.

👩‍💻 Author

Narges