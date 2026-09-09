# 📁 Smart File Organizer

A simple **intermediate-level Python project** that automatically organizes files into separate folders based on their file extensions.

The program helps keep folders such as Downloads or Desktop clean and organized.

## 🚀 Features

* 📂 Automatically organizes files
* 🖼️ Organizes image files
* 📄 Organizes documents
* 📊 Organizes spreadsheets
* 🎬 Organizes videos
* 🎵 Organizes audio files
* 📦 Organizes archive files
* 💻 Organizes programming files
* 📁 Places unknown file types in an `Others` folder
* 🔍 Preview mode before moving files
* 🛡️ Handles duplicate filenames
* ⚠️ Includes error handling
* 📝 Creates an organization log
* 💻 Works on Windows, Linux, and macOS
* 📦 Uses only Python standard libraries

## 📁 Project Structure

```text
File-Organizer/
│
├── file_organizer.py
├── README.md
└── requirements.txt
```

## 🛠️ Technologies Used

* Python 3
* `os`
* `shutil`
* `pathlib`
* `datetime`

No external Python packages are required.

## 📋 File Categories

The program organizes files into the following categories:

| Category     | Examples                                             |
| ------------ | ---------------------------------------------------- |
| Images       | `.jpg`, `.png`, `.gif`, `.webp`                      |
| Documents    | `.pdf`, `.docx`, `.txt`, `.pptx`                     |
| Spreadsheets | `.xls`, `.xlsx`, `.csv`                              |
| Videos       | `.mp4`, `.mkv`, `.avi`, `.mov`                       |
| Audio        | `.mp3`, `.wav`, `.aac`, `.flac`                      |
| Archives     | `.zip`, `.rar`, `.7z`, `.tar`                        |
| Code         | `.py`, `.java`, `.c`, `.cpp`, `.html`, `.css`, `.js` |
| Others       | Unknown file extensions                              |

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installation:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Open the Project Folder

Open the terminal or Command Prompt inside the project folder.

### Step 3: Run the Program

```bash
python file_organizer.py
```

## 💡 How to Use

After starting the program, enter the path of the folder that you want to organize.

Example:

```text
C:\Users\YourName\Downloads
```

Then choose:

```text
1. Preview organization
2. Organize files
3. Exit
```

### Preview Mode

Preview mode shows what the program would do without moving any files.

Example:

```text
📄 photo.jpg → Images/
📄 movie.mp4 → Videos/
📄 notes.txt → Documents/
```

### Organize Mode

The program actually moves the files into their respective folders.

## 📊 Example

Before organizing:

```text
Downloads/
│
├── photo.jpg
├── movie.mp4
├── notes.txt
├── song.mp3
├── program.py
└── backup.zip
```

After organizing:

```text
Downloads/
│
├── Images/
│   └── photo.jpg
│
├── Videos/
│   └── movie.mp4
│
├── Documents/
│   └── notes.txt
│
├── Audio/
│   └── song.mp3
│
├── Code/
│   └── program.py
│
└── Archives/
    └── backup.zip
```

## 🛡️ Duplicate File Handling

The program prevents existing files from being overwritten.

For example, if:

```text
photo.jpg
```

already exists, the new file will be renamed:

```text
photo_1.jpg
```

If that file also exists:

```text
photo_2.jpg
```

The program continues increasing the number until it finds a unique filename.

## ⚠️ Error Handling

The program handles:

* Invalid folder paths
* Empty folder paths
* Paths that are not folders
* Permission errors
* File movement errors
* Duplicate filenames

## 📝 Organization Log

After organizing files, the program creates:

```text
organization_log.txt
```

The log records the time when the organizer was executed.

Example:

```text
File Organizer executed: 2026-09-09 23:45:21
```

## 🧠 Python Concepts Used

This project demonstrates several important Python concepts:

* Dictionaries
* Lists
* Functions
* Loops
* Conditional statements
* Exception handling
* File handling
* Path handling
* String manipulation
* Modules
* `pathlib`
* `shutil`
* Date and time
* User input
* Boolean parameters

## 🔄 Program Flow

```text
Start
  ↓
Get folder path
  ↓
Validate folder
  ↓
Choose operation
  ↓
Scan files
  ↓
Check file extension
  ↓
Find category
  ↓
Create category folder
  ↓
Check duplicate filename
  ↓
Move file
  ↓
Display summary
  ↓
Create log
  ↓
End
```

## 🎯 Project Objective

The main objective of this project is to demonstrate how Python can be used to automate file-management tasks.

It also provides practical experience with file systems, exception handling, functions, dictionaries, and Python's standard library.

## 🔮 Future Improvements

Possible future improvements include:

* Graphical User Interface using Tkinter
* Automatic organization of subfolders
* Custom categories
* Undo last organization
* Detailed logging of every moved file
* Scheduled automatic organization
* Command-line arguments
* File-size based categorization
* Organization by date
* Recursive folder scanning

## 👨‍💻 Author

**Roshan Kumar Yadav**

Created as an intermediate Python project for learning and practicing file handling and automation.