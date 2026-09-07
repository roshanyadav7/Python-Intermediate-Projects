# 🔐 Password Strength Checker

A simple **Python-based Password Strength Checker** that analyzes a password and determines its strength based on basic security requirements.

The project also includes a **Strong Password Generator** that creates random passwords containing uppercase letters, lowercase letters, numbers, and special characters.

## 📌 Features

* 🔍 Check password strength
* 📏 Check password length
* 🔠 Check for uppercase letters
* 🔡 Check for lowercase letters
* 🔢 Check for numbers
* 🔣 Check for special characters
* 📊 Calculate password score out of 5
* 💡 Provide suggestions for improving weak passwords
* 🔐 Generate strong random passwords
* ✅ Simple menu-driven interface
* 🚫 No external Python libraries required

## 🛠️ Technologies Used

* **Python 3**
* `string` module
* `secrets` module

Both modules are built into Python, so no additional installation is required.

## 📋 Password Requirements

The password is checked for five basic requirements:

| Requirement           | Score |
| --------------------- | ----: |
| At least 8 characters |     1 |
| Uppercase letter      |     1 |
| Lowercase letter      |     1 |
| Number                |     1 |
| Special character     |     1 |

### Strength Levels

| Score | Strength       |
| ----: | -------------- |
|   0–2 | 🔴 WEAK        |
|     3 | 🟡 MODERATE    |
|     4 | 🟢 STRONG      |
|     5 | 🟢 VERY STRONG |

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check using:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Download or Clone the Project

Clone the repository:

```bash
git clone https://github.com/your-username/password-strength-checker.git
```

Move into the project folder:

```bash
cd password-strength-checker
```

### 3. Run the Program

On Windows:

```bash
python password_checker.py
```

On Linux/macOS:

```bash
python3 password_checker.py
```

## 💻 Sample Output

```text
========================================
       PASSWORD STRENGTH CHECKER
========================================
1. Check Password Strength
2. Generate Strong Password
3. Exit
========================================
Enter your choice: 1

Enter your password: Hello123

========================================
        PASSWORD ANALYSIS
========================================
Password Length     : 8
Uppercase           : Yes
Lowercase           : Yes
Number              : Yes
Special Character   : No
----------------------------------------
Score               : 4/5
Strength            : STRONG

Suggestions:
- Add at least one special character.
========================================
```

### 🔐 Password Generator Example

```text
========================================
       PASSWORD STRENGTH CHECKER
========================================
1. Check Password Strength
2. Generate Strong Password
3. Exit
========================================
Enter your choice: 2

Enter password length (8-20): 12

========================================
       GENERATED PASSWORD
========================================
a7#Kp2!Lm9Qx
========================================
```

## 📂 Project Structure

```text
Password-Strength-Checker/
│
├── password_checker.py
└── README.md
```

## 🧠 How It Works

The program uses separate checks to analyze the password:

1. **Length Check**
   Checks whether the password contains at least 8 characters.

2. **Uppercase Check**
   Looks for at least one uppercase letter such as `A`, `B`, or `C`.

3. **Lowercase Check**
   Looks for at least one lowercase letter such as `a`, `b`, or `c`.

4. **Number Check**
   Looks for at least one digit from `0` to `9`.

5. **Special Character Check**
   Checks for characters such as `@`, `#`, `$`, `%`, `!`, etc.

6. **Score Calculation**
   Each successful requirement adds one point to the password's score.

7. **Password Generation**
   The generator creates a password containing all four character types and randomly mixes them.

## 🎯 Learning Objectives

This project helps beginners practice:

* Python functions
* `if-elif-else` statements
* `while` loops
* `for` loops
* Lists
* String operations
* `any()` function
* Exception handling
* User input
* Random password generation
* Basic password security concepts

## 🔮 Future Improvements

Some possible improvements are:

* Add password history
* Detect commonly used passwords
* Add a visual strength meter
* Add a GUI using Tkinter
* Allow custom password requirements
* Add a password entropy calculation
* Add password visibility toggle

## ⚠️ Disclaimer

This project is intended for **educational purposes**. The strength checker uses basic password rules and should not be considered a complete professional password-security system.

## 👨‍💻 Author

**Roshan  Kumar Yadav**

---

⭐ If you found this project useful, consider giving it a star on GitHub!