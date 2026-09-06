# 🎓 Student Management System

A simple **Intermediate-level Student Management System** built using **Python**.

The project allows you to manage student records, marks, grades, and academic performance through a command-line interface.

## 📌 Features

* ➕ Add new students
* 👀 View all students
* 🔍 Search students by ID or name
* ✏️ Update student information
* 🗑️ Delete student records
* 📊 Calculate total marks and average
* 🏆 Automatically assign grades
* 🥇 Find the class topper
* 💾 Save student data permanently using JSON
* 🔒 Validate user input
* 📋 Clean and easy-to-use menu system

## 🛠️ Technologies Used

* **Python 3**
* **JSON** for data storage
* **OS module** for file handling
* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Exception handling
* Lambda functions

## 📂 Project Structure

```text
Student Management System/
│
├── student_management_system.py
├── students.json
└── README.md
```

### `student_management_system.py`

Contains the complete Python program and all student management operations.

### `students.json`

Stores student information permanently so that the data is available even after closing the program.

### `README.md`

Contains information about the project, its features, installation, and usage.

## 📊 Student Information

Each student record contains:

* Student ID
* Name
* Age
* Course
* Python marks
* Java marks
* Mathematics marks
* Total marks
* Average marks
* Grade

### Example

```text
Student ID : 101
Name       : Roshan
Age        : 21
Course     : B.Tech CSE

Python     : 85
Java       : 99
Mathematics: 92

Total      : 255
Average    : 85.00
Grade      : A
Result     : PASS
```

## 🏆 Grading System

|  Average | Grade |
| :------: | :---: |
| 90 – 100 |   A+  |
|  80 – 89 |   A   |
|  70 – 79 |   B   |
|  60 – 69 |   C   |
|  50 – 59 |   D   |
| Below 50 |   F   |

## 🚀 How to Run

### 1. Install Python

Make sure **Python 3** is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Download or Clone the Project

Place the project files inside a folder:

```text
Student Management System/
```

### 3. Open the Terminal

Navigate to the project folder:

```bash
cd "Student Management System"
```

### 4. Run the Program

Run the following command:

```bash
python student_management_system.py
```

## 🖥️ Main Menu

When the program starts, you will see:

```text
========================================
       STUDENT MANAGEMENT SYSTEM
========================================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Find Topper
7. Exit
========================================
```

## 💾 Data Storage

The project uses a JSON file named:

```text
students.json
```

Whenever a student is added, updated, or deleted, the program saves the changes to this file.

### Example JSON Structure

```json
[
    {
        "id": "101",
        "name": "Rahul",
        "age": 20,
        "course": "B.Tech CSE",
        "marks": {
            "Python": 85,
            "Java": 78,
            "Mathematics": 92
        },
        "total": 255,
        "average": 85.0,
        "grade": "A"
    }
]
```

This means the student data **does not disappear when the program is closed**.

## 🧠 Concepts Practiced

This project is useful for practicing several important Python concepts.

### Functions

The program is divided into separate functions such as:

```python
add_student()
view_students()
search_student()
update_student()
delete_student()
find_topper()
```

### Lists

Students are stored inside a list:

```python
students = []
```

### Dictionaries

Each student is represented using a dictionary:

```python
student = {
    "id": "101",
    "name": "Rahul",
    "age": 20
}
```

### Exception Handling

Invalid user input is handled using:

```python
try:
    ...
except ValueError:
    ...
```

### JSON

Student records are stored permanently using:

```python
json.dump()
json.load()
```

### Lambda Function

The topper is found using:

```python
max(students, key=lambda student: student["average"])
```

## 🔄 Program Flow

```text
Start
  ↓
Load students from JSON
  ↓
Display Main Menu
  ↓
Choose an operation
  ↓
Add / View / Search / Update / Delete / Topper
  ↓
Save changes to JSON
  ↓
Return to Main Menu
  ↓
Exit
```

## 🔐 Input Validation

The program checks user input before accepting it.

For example:

* Student ID cannot be duplicated
* Name cannot be empty
* Age must be within a valid range
* Marks must be between `0` and `100`
* Invalid numeric input is handled safely
* Delete operation requires confirmation

## 🎯 Project Level

| Category      | Details                      |
| ------------- | ---------------------------- |
| **Level**     | Intermediate                 |
| **Language**  | Python                       |
| **Interface** | Command Line Interface (CLI) |
| **Storage**   | JSON File                    |

## 🔮 Future Improvements

The project can be further improved by adding:

* 👤 Admin login system
* 📚 More subjects
* 📈 Student performance reports
* 📊 Graphs and charts
* 🏫 Department management
* 📅 Attendance management
* 💰 Fee management
* 🗄️ SQLite/MySQL database
* 🖥️ GUI using Tkinter
* 🌐 Web version using Flask or Django

## 👨‍💻 Author

**Roshan Kumar Yadav**

**Student Management System – Python Project**

Built as an intermediate-level Python project for learning and practicing Python programming concepts.
