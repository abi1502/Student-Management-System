# Student Management System

A console-based **Student Management System** developed using Python.
The project allows users to manage student records, perform academic calculations, search and sort students, store data in JSON, and export student information to CSV.

## Features

* Add Student
* Display All Students
* Search Student by Roll Number
* Search Student by Name
* Search Students by Course
* Update Student Details
* Delete Student
* Calculate Grade
* Check Pass / Fail
* Calculate Average Mark
* Find Highest Mark
* Find Lowest Mark
* Count Total Students
* Sort Students by Mark
* Sort Students by Name
* Generate Student Report
* Calculate Attendance Percentage
* Student Dashboard
* Save and Load Data using JSON
* Export Student Data to CSV
* Unique Roll Number Validation

## Technologies Used

* Python 3
* JSON
* CSV
* Python Standard Library

## Python Concepts Used

* Variables and Data Types
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* List Comprehension
* Lambda Functions
* Sorting
* File Handling
* JSON Handling
* CSV Handling
* Exception Handling
* Modules and Imports

## Project Structure

```text
Student_Management_System/
│
├── main.py
├── student.py
├── data.json
├── students.csv
└── README.md
```

### File Description

**main.py**
Contains the main menu and controls the Student Management System.

**student.py**
Contains student data and all major functions such as add, search, update, delete, sorting, reports, dashboard, JSON handling, and CSV export.

**data.json**
Stores student information in JSON format.

**students.csv**
Stores exported student information in CSV format.

**README.md**
Contains project documentation and instructions.

## How to Run

1. Download or clone the project.
2. Open the project folder.
3. Open `main.py` using Python IDLE or another Python editor.
4. Run `main.py`.
5. Select an option from the menu.

## Main Menu

```text
1. Add Student
2. Display Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Grade
7. Pass / Fail
8. Average Mark
9. Highest Mark
10. Lowest Mark
11. Count Students
12. Search by Course
13. Search by Name
14. Sort by Mark
15. Sort by Name
16. Student Report
17. Attendance
18. Save Data
19. Student Dashboard
20. Export to CSV
21. Exit
```

## Data Storage

Student records are stored in `data.json`.

The project also provides a CSV export feature. Selecting **Export to CSV** creates/updates `students.csv`, which can be opened using Microsoft Excel or other spreadsheet applications.

## Sample Student Data

| Roll No | Name  | Age | Course | Mark |
| ------- | ----- | --: | ------ | ---: |
| 101     | Abi   |  21 | BCA    |   85 |
| 102     | Priya |  20 | BCA    |   92 |
| 103     | Rahul |  22 | Python |   78 |

## Project Highlights

* Menu-driven Python application
* CRUD operations for student records
* JSON-based data persistence
* CSV data export
* Search and sorting functionality
* Academic grade and result calculation
* Attendance calculation
* Student performance dashboard
* Roll number validation

## Future Improvements

* Add a graphical user interface using Tkinter
* Connect the project with MySQL
* Add user login and authentication
* Add a web interface using Flask or Django
* Add more student performance reports

## Author

**Abivarshini B**

BCA Graduate | Python | SQL | HTML | CSS | JavaScript | React.js
