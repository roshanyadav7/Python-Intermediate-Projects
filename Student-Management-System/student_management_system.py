import json
import os


DATA_FILE = "students.json"


# --------------------------------------------------
# Load students from JSON file
# --------------------------------------------------

def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


# --------------------------------------------------
# Save students to JSON file
# --------------------------------------------------

def save_students(students):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(students, file, indent=4)

        print("\nData saved successfully!")

    except OSError:
        print("\nError: Unable to save data.")


# --------------------------------------------------
# Calculate grade
# --------------------------------------------------

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# --------------------------------------------------
# Calculate student performance
# --------------------------------------------------

def calculate_performance(marks):
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    return total, average, grade


# --------------------------------------------------
# Get valid marks
# --------------------------------------------------

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# --------------------------------------------------
# Add student
# --------------------------------------------------

def add_student(students):

    print("\n" + "=" * 50)
    print("                 ADD STUDENT")
    print("=" * 50)

    while True:
        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            continue

        if any(student["id"] == student_id for student in students):
            print("Student ID already exists.")
            continue

        break

    while True:
        name = input("Enter Student Name: ").strip()

        if name:
            break

        print("Name cannot be empty.")

    while True:
        try:
            age = int(input("Enter Age: "))

            if 15 <= age <= 100:
                break

            print("Enter a valid age.")

        except ValueError:
            print("Please enter a valid number.")

    course = input("Enter Course: ").strip()

    if not course:
        course = "Not Specified"

    subjects = ["Python", "Java", "Mathematics"]

    marks = {}

    for subject in subjects:
        marks[subject] = get_marks(subject)

    total, average, grade = calculate_performance(
        list(marks.values())
    )

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

    save_students(students)

    print("\nStudent added successfully!")
    print(f"Total   : {total}")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")


# --------------------------------------------------
# Display one student
# --------------------------------------------------

def display_student(student):

    print("\n" + "-" * 50)

    print(f"Student ID : {student['id']}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"Course     : {student['course']}")

    print("\nMarks:")

    for subject, marks in student["marks"].items():
        print(f"  {subject:<15}: {marks:g}")

    print(f"\nTotal      : {student['total']}")
    print(f"Average    : {student['average']:.2f}")
    print(f"Grade      : {student['grade']}")

    result = "PASS" if student["grade"] != "F" else "FAIL"
    print(f"Result     : {result}")

    print("-" * 50)


# --------------------------------------------------
# View all students
# --------------------------------------------------

def view_students(students):

    if not students:
        print("\nNo students found.")
        return

    print("\n" + "=" * 70)
    print("                       ALL STUDENTS")
    print("=" * 70)

    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Course':<20}"
        f"{'Average':<10}"
        f"{'Grade':<10}"
    )

    print("-" * 70)

    for student in students:
        print(
            f"{student['id']:<10}"
            f"{student['name']:<20}"
            f"{student['course']:<20}"
            f"{student['average']:<10.2f}"
            f"{student['grade']:<10}"
        )


# --------------------------------------------------
# Search student
# --------------------------------------------------

def search_student(students):

    if not students:
        print("\nNo students available.")
        return

    search = input(
        "\nEnter Student ID or Name to search: "
    ).strip().lower()

    found = []

    for student in students:

        if (
            search == student["id"].lower()
            or search in student["name"].lower()
        ):
            found.append(student)

    if not found:
        print("\nStudent not found.")
        return

    for student in found:
        display_student(student)


# --------------------------------------------------
# Update student
# --------------------------------------------------

def update_student(students):

    student_id = input("\nEnter Student ID to update: ").strip()

    student = None

    for item in students:
        if item["id"] == student_id:
            student = item
            break

    if student is None:
        print("\nStudent not found.")
        return

    print("\nLeave a field empty to keep the existing value.")

    name = input(f"Name [{student['name']}]: ").strip()

    if name:
        student["name"] = name

    age_input = input(f"Age [{student['age']}]: ").strip()

    if age_input:
        try:
            age = int(age_input)

            if 15 <= age <= 100:
                student["age"] = age
            else:
                print("Invalid age. Keeping old value.")

        except ValueError:
            print("Invalid age. Keeping old value.")

    course = input(
        f"Course [{student['course']}]: "
    ).strip()

    if course:
        student["course"] = course

    print("\nUpdate marks?")

    choice = input("Enter Y/N: ").strip().lower()

    if choice == "y":

        for subject in student["marks"]:
            student["marks"][subject] = get_marks(subject)

        (
            student["total"],
            student["average"],
            student["grade"]
        ) = calculate_performance(
            list(student["marks"].values())
        )

    save_students(students)

    print("\nStudent updated successfully!")


# --------------------------------------------------
# Delete student
# --------------------------------------------------

def delete_student(students):

    student_id = input(
        "\nEnter Student ID to delete: "
    ).strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent found:")
            display_student(student)

            confirmation = input(
                "Are you sure you want to delete this student? (Y/N): "
            ).strip().lower()

            if confirmation == "y":

                students.remove(student)
                save_students(students)

                print("\nStudent deleted successfully!")

            else:
                print("\nDeletion cancelled.")

            return

    print("\nStudent not found.")


# --------------------------------------------------
# Find topper
# --------------------------------------------------

def find_topper(students):

    if not students:
        print("\nNo students available.")
        return

    topper = max(
        students,
        key=lambda student: student["average"]
    )

    print("\n" + "=" * 50)
    print("                    TOPPER")
    print("=" * 50)

    display_student(topper)


# --------------------------------------------------
# Main menu
# --------------------------------------------------

def main():

    students = load_students()

    while True:

        print("\n")
        print("=" * 55)
        print("              STUDENT MANAGEMENT SYSTEM")
        print("=" * 55)

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Find Topper")
        print("7. Save Data")
        print("8. Exit")

        print("-" * 55)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            find_topper(students)

        elif choice == "7":
            save_students(students)

        elif choice == "8":
            save_students(students)
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice. Please select 1-8.")


# --------------------------------------------------
# Program starts here
# --------------------------------------------------

if __name__ == "__main__":
    main()