# 🔗 URL Status Checker

A simple **intermediate-level Python project** that checks the status and availability of websites.

The program sends an HTTP request to a URL and provides useful information such as the HTTP status code, website status, response time, HTTPS availability, and number of redirects.

---

## 📌 Features

* 🔗 Check a single URL
* 🌐 Check multiple URLs
* ✅ Detect whether a website is online
* 📊 Display HTTP status codes
* ⏱️ Measure response time
* 🔒 Check HTTPS usage
* ↪️ Detect redirects
* ❌ Handle invalid URLs
* ⚠️ Handle connection errors
* ⏳ Handle timeout errors
* 📋 Display a summary for multiple URLs
* 🖥️ Simple command-line interface

---

## 🛠️ Technologies Used

* **Python 3**
* **Requests**
* **urllib**
* **time**

---

## 📂 Project Structure

```text
URL-Status-Checker/
│
├── url_status_checker.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/roshanyadav7/Python-Intermediate-Projects.git
```

### 2. Open the project directory

```bash
cd URL-Status-Checker
```

### 3. Install the required library

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the Python file:

```bash
python url_status_checker.py
```

The program will display the main menu:

```text
==================================================
              URL STATUS CHECKER
==================================================
1. Check a URL
2. Check multiple URLs
3. Exit

Enter your choice:
```

---

## 💻 Example 1: Checking a Single URL

```text
==================================================
              URL STATUS CHECKER
==================================================

1. Check a URL
2. Check multiple URLs
3. Exit

Enter your choice: 1

Enter URL: https://www.google.com

Checking URL...
--------------------------------------------------
URL            : https://www.google.com
Status Code    : 200
Status         : ONLINE
Response Time  : 0.42 seconds
HTTPS          : YES
Redirects      : 0
```

---

## 💻 Example 2: Checking Multiple URLs

```text
Enter your choice: 2

Enter URLs separated by commas:
https://www.google.com, https://www.github.com

Checking URL...
--------------------------------------------------
URL            : https://www.google.com
Status Code    : 200
Status         : ONLINE
Response Time  : 0.41 seconds
HTTPS          : YES
Redirects      : 0

Checking URL...
--------------------------------------------------
URL            : https://www.github.com
Status Code    : 200
Status         : ONLINE
Response Time  : 0.58 seconds
HTTPS          : YES
Redirects      : 0

============================================================
                    SUMMARY
============================================================
https://www.google.com             200 - ONLINE
https://www.github.com             200 - ONLINE
```

> Response time can be different on every run depending on your internet connection and the server.

---

## ❌ Error Handling

The program handles several common problems.

### Invalid URL

```text
Enter URL: hello

Checking URL...
--------------------------------------------------
```

The program automatically adds `https://` when appropriate.

For an invalid address:

```text
Invalid URL!
```

### Connection Error

If the website cannot be reached:

```text
URL            : https://example-invalid-site.com
Status         : OFFLINE
Error          : Could not connect to the website.
```

### Timeout Error

If the server takes too long:

```text
Status         : TIMEOUT
Error          : The server took too long to respond.
```

---

## 📊 HTTP Status Codes

The project groups HTTP status codes into four major categories.

| Status Code | Meaning            | Program Status |
| ----------- | ------------------ | -------------- |
| 200–299     | Successful request | ONLINE         |
| 300–399     | Redirection        | REDIRECT       |
| 400–499     | Client error       | CLIENT ERROR   |
| 500–599     | Server error       | SERVER ERROR   |

For example:

```text
200 → ONLINE
301 → REDIRECT
404 → CLIENT ERROR
500 → SERVER ERROR
```

---

## 🧠 Python Concepts Used

This project helps practice several important Python concepts:

### Functions

The project is divided into functions such as:

```python
validate_url()
get_status_message()
check_url()
check_multiple_urls()
main()
```

This makes the program easier to understand and maintain.

### Exception Handling

The `try-except` block handles network problems:

```python
try:
    response = requests.get(url, timeout=10)

except requests.exceptions.Timeout:
    ...
```

### Lists and Dictionaries

Results from checked websites are stored using dictionaries:

```python
{
    "url": url,
    "status_code": response.status_code,
    "status": status,
    "response_time": response_time
}
```

### Loops

The program uses loops to:

* Keep the menu running
* Check multiple URLs
* Display results

### HTTP Requests

The `requests` library is used to communicate with websites:

```python
response = requests.get(url, timeout=10)
```

### Time Measurement

The `time` module measures how long a website takes to respond:

```python
start_time = time.time()

response = requests.get(url)

end_time = time.time()
```

---

## 🔍 How It Works

The basic process is:

```text
User enters URL
       ↓
Validate URL
       ↓
Send HTTP request
       ↓
Wait for response
       ↓
Read status code
       ↓
Measure response time
       ↓
Check HTTPS
       ↓
Count redirects
       ↓
Display result
```

---

## 🎯 Learning Objectives

After completing this project, you should understand:

* How HTTP requests work
* What HTTP status codes mean
* How to use the `requests` library
* How to handle network errors
* How to measure execution time
* How to validate URLs
* How to organize a Python project using functions
* How to work with dictionaries and lists
* How to create a command-line application

---

## 🚀 Possible Future Improvements

The project can be extended with:

* 📄 Save results to a CSV file
* 📝 Generate a report
* 🔄 Automatically check URLs at regular intervals
* 📈 Track website response time
* 🟢 Add colored terminal output
* 🔍 Check website SSL certificate information
* 📊 Create response-time statistics
* 🖥️ Add a graphical user interface

---

## ⚠️ Note

This project only checks whether a URL responds to an HTTP request. A successful HTTP response does not necessarily mean that every part of the website is functioning correctly.

---

## 👨‍💻 Author

**Roshan Kumar Yadav**

Created as an intermediate Python project for practicing networking, HTTP requests, exception handling, and command-line programming.