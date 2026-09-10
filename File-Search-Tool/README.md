# 🔎 Smart File Search Tool

A **command-line based file searching application built with Python** that allows users to quickly find files inside a selected directory and its subdirectories.

The tool provides multiple search options, including filename search, extension filtering, combined filename and extension search, file-size filtering, and displaying all available files.

It also provides a **colorful terminal interface**, file information, error handling, and support for searching multiple file extensions at the same time.

---

## 📌 Project Overview

Finding a specific file inside a large folder structure can be time-consuming when done manually.

The **Smart File Search Tool** solves this problem by recursively scanning a selected folder and providing different ways to filter and locate files.

The project was developed using Python's built-in modules, making it lightweight and easy to run without installing external libraries.

---

## ✨ Features

* 🔍 Search files by filename
* 📂 Search through folders and subfolders
* 🧩 Search files by extension
* 📑 Support multiple file extensions
* 🔎 Search using filename + extension
* 📏 Find files larger than a specified size
* 📋 Display all files in a directory
* 📊 Display file size
* 📅 Display last modified date and time
* 📍 Display complete file path
* 🎨 Colored terminal interface
* 🔄 Change the search folder without restarting
* ⚠️ Handle invalid paths
* 🛡️ Handle permission errors
* ❌ Handle invalid user input
* 💻 Works on Windows, Linux, and macOS

---

## 🛠️ Technologies Used

| Technology        | Purpose                             |
| ----------------- | ----------------------------------- |
| Python 3          | Main programming language           |
| `pathlib`         | File and directory operations       |
| `os`              | Operating-system related operations |
| `datetime`        | File modification date and time     |
| ANSI Escape Codes | Terminal colors                     |

---

## 📁 Project Structure

```text
Smart-File-Search-Tool/
│
├── file_search_tool.py
│
├── README.md
│
├── requirements.txt
│
└── .gitignore
```

### File Description

**`file_search_tool.py`**

Contains the complete Python application and all search functionality.

**`README.md`**

Contains project documentation, installation instructions, features, and usage information.

**`requirements.txt`**

Contains project dependencies.

**`.gitignore`**

Contains files and folders that should not be uploaded to GitHub.

---

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.8 or newer
* Command Prompt / PowerShell / Terminal

No external Python libraries are required.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/roshanyadav7/Python-Intermediate-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd Smart-File-Search-Tool
```

### 3. Run the Program

```bash
python file_search_tool.py
```

---

## 📦 Dependencies

This project uses only Python's built-in modules.

Therefore, no additional packages need to be installed.

The `requirements.txt` file contains:

```text
# No external dependencies required
```

---

# 🖥️ How to Use

After starting the program, enter the path of the folder you want to search.

Example:

```text
Enter folder path: C:\Users\Roshan\Documents
```

The application will then display the main menu.

```text
============================================================
             SMART FILE SEARCH TOOL
============================================================

Current Folder: C:\Users\Roshan\Documents

1. Search by filename
2. Search by extension
3. Search by filename + extension
4. Find files larger than a size
5. Show all files
6. Change folder
7. Exit

Enter your choice:
```

---

# 🔍 Search Options

## 1. Search by Filename

Search for files based on a keyword in their filename.

Example:

```text
Enter filename keyword: python
```

The program may find:

```text
python.py
python_notes.txt
my_python_project.py
python_assignment.pdf
```

The search is **case-insensitive**, so searching for:

```text
Python
```

and:

```text
python
```

will produce the same results.

---

## 2. Search by Extension

Search for files based on their extension.

The program supports **multiple extensions**.

Example:

```text
Enter extensions separated by commas:
.py,.txt,.pdf
```

This searches for:

```text
.py
.txt
.pdf
```

You can also enter extensions without the `.`:

```text
py,txt,pdf
```

The program automatically adds the required dot.

---

## 3. Search by Filename + Extension

This option combines two filters.

For example:

```text
Enter filename keyword: project

Enter extensions separated by commas:
.py,.txt
```

The program searches for files that:

1. Contain `project` in their filename
2. Have either `.py` or `.txt` extension

Possible results:

```text
project.py
my_project.py
project_notes.txt
python_project.txt
```

---

## 4. Find Files Larger Than a Specific Size

This option searches for files larger than a specified size in megabytes.

Example:

```text
Find files larger than (MB): 10
```

The program will display files larger than **10 MB**.

Example output:

```text
------------------------------------------------------------
Files Found: 2
------------------------------------------------------------

1. video.mp4
   Location : C:\Users\Roshan\Videos\video.mp4
   Size     : 245.30 MB
   Modified : 2026-09-10 18:20:31

2. backup.zip
   Location : C:\Users\Roshan\Downloads\backup.zip
   Size     : 125.60 MB
   Modified : 2026-09-09 14:10:25

------------------------------------------------------------
Total files found: 2
------------------------------------------------------------
```

---

## 5. Show All Files

This option displays every file inside the selected folder and its subfolders.

For example:

```text
Documents/
│
├── notes.txt
├── resume.pdf
│
├── Python/
│   ├── program.py
│   └── project.py
│
└── College/
    ├── assignment.docx
    └── report.pdf
```

The program recursively searches all these directories.

---

## 6. Change Folder

You don't need to restart the application to search another folder.

Select:

```text
6. Change folder
```

Then enter another path.

Example:

```text
Enter folder path:
D:\Projects
```

The new folder becomes the current search location.

---

## 📊 Example Output

```text
============================================================
             SMART FILE SEARCH TOOL
============================================================

Current Folder: C:\Users\Roshan\Documents

1. Search by filename
2. Search by extension
3. Search by filename + extension
4. Find files larger than a size
5. Show all files
6. Change folder
7. Exit

Enter your choice: 2

Enter extensions separated by commas (example: .py,.txt,.pdf):
.py,.txt,.pdf

------------------------------------------------------------
Files Found: 3
------------------------------------------------------------

1. python.py
   Location : C:\Users\Roshan\Documents\python.py
   Size     : 4.21 KB
   Modified : 2026-09-10 18:20:31

2. notes.txt
   Location : C:\Users\Roshan\Documents\College\notes.txt
   Size     : 2.45 KB
   Modified : 2026-09-09 20:15:12

3. assignment.pdf
   Location : C:\Users\Roshan\Documents\College\assignment.pdf
   Size     : 1.25 MB
   Modified : 2026-09-08 15:30:10

------------------------------------------------------------
Total files found: 3
------------------------------------------------------------
```

---

# 🧠 Concepts Demonstrated

This project demonstrates several important Python programming concepts.

### Functions

The application is divided into separate functions for better organization.

Examples:

```python
search_by_filename()
search_by_extension()
search_by_size()
display_results()
```

### Object-Oriented File Paths

The project uses Python's `pathlib` module.

```python
from pathlib import Path
```

Example:

```python
folder_path = Path(folder)
```

### Recursive File Searching

The following method searches the selected directory and its subdirectories:

```python
folder.rglob("*")
```

This allows the program to search through an entire folder structure.

### File Extension Filtering

The file extension can be obtained using:

```python
file_path.suffix
```

For example:

```text
program.py  →  .py
notes.txt   →  .txt
report.pdf  →  .pdf
```

### File Information

The program retrieves file information using:

```python
file_path.stat()
```

This allows the application to obtain:

* File size
* Last modified time

### Exception Handling

The project handles common errors using:

```python
try:
    ...
except:
    ...
```

This prevents the program from crashing when it encounters invalid input or inaccessible files.

### String Processing

The project uses string methods such as:

```python
.lower()
.strip()
.split(",")
```

These are used to process user input and perform case-insensitive searches.

---

# 🏗️ Program Workflow

```text
              START
                │
                ▼
       Enter Folder Path
                │
                ▼
       Validate Folder
                │
          ┌─────┴─────┐
          │           │
       Invalid       Valid
          │           │
          ▼           ▼
        Error       Main Menu
                      │
          ┌───────────┼────────────┐
          ▼           ▼            ▼
      Filename    Extension      Size
       Search       Search       Search
          │           │            │
          └───────────┼────────────┘
                      │
                      ▼
              Search Subfolders
                      │
                      ▼
              Display Results
                      │
                      ▼
                  Main Menu
                      │
                      ▼
                    EXIT
```

---

# 🔐 Error Handling

The application handles several common problems.

### Invalid Folder

```text
Error: Folder does not exist.
```

### Path Is Not a Directory

```text
Error: The path is not a folder.
```

### Empty Filename Keyword

```text
Keyword cannot be empty.
```

### Invalid File Size

```text
Please enter a valid number.
```

### Permission Error

```text
Permission denied while searching.
```

This makes the application more reliable and user-friendly.

---

# 🚀 Future Improvements

The project can be expanded with additional features such as:

* 🔤 Sort results alphabetically
* 📅 Search by creation date
* 📅 Search by modification date
* 🔎 Search inside file contents
* 📄 Preview text files
* 📊 Export search results to CSV
* 📋 Save search history
* 🗑️ Delete selected files
* 📁 Copy or move files
* 🔁 Find duplicate files
* 🖥️ Build a graphical interface using Tkinter
* ⚡ Add multithreading for faster searching
* 📈 Display search statistics

---

# 🎯 Learning Outcomes

After completing this project, you will understand how to:

* Work with files and directories using Python
* Traverse directories recursively
* Use `pathlib`
* Retrieve file metadata
* Process user input
* Build menu-driven applications
* Handle exceptions
* Work with lists and loops
* Create reusable functions
* Format terminal output
* Build a practical Python command-line application

---

# 🧪 Testing

The program should be tested with:

| Test                         | Expected Result                    |
| ---------------------------- | ---------------------------------- |
| Valid folder                 | Folder opens successfully          |
| Invalid folder               | Error message displayed            |
| Empty filename               | Error message displayed            |
| `.py,.txt`                   | Both extensions searched           |
| `py,txt`                     | Extensions automatically formatted |
| Valid size                   | Files larger than size displayed   |
| Invalid size                 | Input error displayed              |
| Empty extension              | Error message displayed            |
| Permission-restricted folder | Permission error handled           |
| Exit option                  | Program terminates                 |

---

# 💡 Why This Is an Intermediate Project

This project goes beyond basic Python file handling.

It combines:

```text
Python Basics
     +
Functions
     +
File Handling
     +
Pathlib
     +
Recursive Searching
     +
Filtering
     +
Exception Handling
     +
File Metadata
     +
User Input
     +
Terminal UI
```

This makes it suitable as an **intermediate Python project for learning, GitHub, portfolio development, or college submission**.

---

# 👨‍💻 Author

**Roshan Kumar Yadav**

---

# 📄 License

This project is created for **educational and learning purposes**.
