# 📱 Contact Book

A command-line **Contact Book application built with Python** that allows users to add, view, search, update, and delete contacts. Contact data is stored permanently in a JSON file so that it remains available after the program is closed.

## ✨ Features

* ➕ Add new contacts
* 👀 View all saved contacts
* 🔍 Search contacts by name or phone number
* ✏️ Update existing contact information
* 🗑️ Delete contacts with confirmation
* 💾 Persistent data storage using JSON
* ✅ Name validation
* 📱 10-digit phone number validation
* 📧 Basic email validation
* 🚫 Prevent duplicate phone numbers
* ⚠️ Handles missing or invalid JSON files
* 🖥️ Simple command-line interface

## 🛠️ Technologies Used

* **Python 3**
* **JSON**
* **File Handling**
* **Functions**
* **Lists & Dictionaries**
* **Exception Handling**

## 📂 Project Structure

```text
Contact-Book/
│
├── contact_book.py
├── contacts.json
└── README.md
```

### Files

**`contact_book.py`**
Contains the complete Contact Book application.

**`contacts.json`**
Stores contact information permanently.

**`README.md`**
Project documentation.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/roshanyadav7/Python-Intermediate-Projects.git
```

### 2. Navigate to the project

```bash
cd Python-Intermediate-Projects/Contact-Book
```

### 3. Run the program

```bash
python contact_book.py
```

## 📋 Menu

```text
==================================================
                CONTACT BOOK
==================================================

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
```

## 💾 Data Storage

Contacts are stored in `contacts.json` using JSON format.

Example:

```json
[
    {
        "name": "Roshan",
        "phone": "9800000000",
        "email": "roshan@example.com",
        "address": "Janakpur"
    }
]
```

The program automatically loads saved contacts when it starts and saves changes whenever a contact is added, updated, or deleted.

## 🧠 Concepts Practiced

This project helped me practice several important Python concepts:

* Variables and data types
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* String methods
* Input validation
* File handling
* JSON serialization and deserialization
* `try` / `except`
* Working with persistent data

## 🔮 Future Improvements

Possible features for future versions:

* 🆔 Unique contact IDs
* 🔤 Sort contacts alphabetically
* 📞 Search by multiple fields
* 👥 Support duplicate names using contact IDs
* 📧 Stronger email validation
* 🌍 International phone number support
* 🎨 Improved terminal interface
* 📊 Contact categories/groups
* 🔐 Password-protected contacts

## 👨‍💻 Author

**Roshan Kumar Yadav**

GitHub: [@roshanyadav7](https://github.com/roshanyadav7)

---

⭐ If you found this project useful, consider giving the repository a star!