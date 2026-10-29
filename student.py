import json


students = [
    {"roll_no": "101", "name": "Abi", "age": 21, "course": "BCA", "mark": 85},
    {"roll_no": "102", "name": "Priya", "age": 20, "course": "BCA", "mark": 92},
    {"roll_no": "103", "name": "Rahul", "age": 22, "course": "Python", "mark": 78},
    {"roll_no": "104", "name": "Anu", "age": 21, "course": "BCA", "mark": 88},
    {"roll_no": "105", "name": "Karthik", "age": 22, "course": "Python", "mark": 74},
    {"roll_no": "106", "name": "Divya", "age": 20, "course": "BCA", "mark": 95},
    {"roll_no": "107", "name": "Arun", "age": 21, "course": "Python", "mark": 81},
    {"roll_no": "108", "name": "Meena", "age": 22, "course": "BCA", "mark": 69},
    {"roll_no": "109", "name": "Vijay", "age": 21, "course": "Python", "mark": 87},
    {"roll_no": "110", "name": "Sneha", "age": 20, "course": "BCA", "mark": 91},
    {"roll_no": "111", "name": "Ravi", "age": 22, "course": "Python", "mark": 76},
    {"roll_no": "112", "name": "Keerthi", "age": 21, "course": "BCA", "mark": 89},
    {"roll_no": "113", "name": "Surya", "age": 23, "course": "Python", "mark": 72},
    {"roll_no": "114", "name": "Nisha", "age": 20, "course": "BCA", "mark": 94},
    {"roll_no": "115", "name": "Aravind", "age": 22, "course": "Python", "mark": 83},
    {"roll_no": "116", "name": "Swetha", "age": 21, "course": "BCA", "mark": 79},
    {"roll_no": "117", "name": "Mohan", "age": 23, "course": "Python", "mark": 68},
    {"roll_no": "118", "name": "Harini", "age": 20, "course": "BCA", "mark": 96},
    {"roll_no": "119", "name": "Sanjay", "age": 22, "course": "Python", "mark": 75},
    {"roll_no": "120", "name": "Pavithra", "age": 21, "course": "BCA", "mark": 90}
]


# Add Student
def add_student():
    print("\n--- ADD STUDENT ---")

    roll_no = input("Enter Roll No: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Roll No already exists!")
            return

    name = input("Enter Name: ")

    while True:
        age = int(input("Enter Age: "))
        if age > 0:
            break
        print("Age must be greater than 0.")

    course = input("Enter Course: ")

    while True:
        mark = float(input("Enter Mark: "))
        if 0 <= mark <= 100:
            break
        print("Mark must be between 0 and 100.")

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "mark": mark
    }

    students.append(student)

    print("Student added successfully!")


# Display Students
def display_students():
    print("\n--- STUDENT LIST ---")

    if len(students) == 0:
        print("No students found.")
        return

    print("-" * 75)
    print(f"{'ID':<8}{'NAME':<15}{'AGE':<8}{'COURSE':<15}{'MARK':<10}")
    print("-" * 75)

    for student in students:
        print(f"{student['roll_no']:<8}"
              f"{student['name']:<15}"
              f"{student['age']:<8}"
              f"{student['course']:<15}"
              f"{student['mark']:<10}")

    print("-" * 75)


# Search Student
def search_student():
    print("\n--- SEARCH STUDENT ---")

    roll_no = input("Enter Roll No: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Roll No :", student["roll_no"])
            print("Name    :", student["name"])
            print("Age     :", student["age"])
            print("Course  :", student["course"])
            print("Mark    :", student["mark"])
            return

    print("Student not found.")


# Update Student
def update_student():
    print("\n--- UPDATE STUDENT ---")

    roll_no = input("Enter Roll No: ")

    for student in students:
        if student["roll_no"] == roll_no:

            print("\nStudent Found!")
            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Course")
            print("4. Update Mark")
            print("5. Cancel")

            choice = input("Enter your choice: ")

            if choice == "1":
                student["name"] = input("Enter New Name: ")
                print("Name updated successfully!")

            elif choice == "2":
                while True:
                    age = int(input("Enter New Age: "))

                    if age > 0:
                        student["age"] = age
                        print("Age updated successfully!")
                        break

                    print("Age must be greater than 0.")

            elif choice == "3":
                student["course"] = input("Enter New Course: ")
                print("Course updated successfully!")

            elif choice == "4":
                while True:
                    mark = float(input("Enter New Mark: "))

                    if 0 <= mark <= 100:
                        student["mark"] = mark
                        print("Mark updated successfully!")
                        break

                    print("Mark must be between 0 and 100.")

            elif choice == "5":
                print("Update cancelled.")

            else:
                print("Invalid choice!")

            return

    print("Student not found.")


# Delete Student
def delete_student():
    print("\n--- DELETE STUDENT ---")

    roll_no = input("Enter Roll No: ")

    for student in students:
        if student["roll_no"] == roll_no:

            print("Student Found!")
            print("Name :", student["name"])

            confirm = input("Are you sure you want to delete? (yes/no): ")

            if confirm.lower() == "yes":
                students.remove(student)
                print("Student deleted successfully!")
            else:
                print("Delete cancelled.")

            return

    print("Student not found.")


# Calculate Grade
def calculate_grade():
    print("\n--- CALCULATE GRADE ---")

    roll_no = input("Enter Roll No: ")

    for student in students:
        if student["roll_no"] == roll_no:

            mark = student["mark"]

            if mark >= 90:
                grade = "A+"
            elif mark >= 80:
                grade = "A"
            elif mark >= 70:
                grade = "B"
            elif mark >= 60:
                grade = "C"
            elif mark >= 50:
                grade = "D"
            else:
                grade = "F"

            print("Name  :", student["name"])
            print("Mark  :", student["mark"])
            print("Grade :", grade)

            return

    print("Student not found.")


# Pass or Fail
def pass_fail():
    print("\n--- PASS / FAIL ---")

    roll_no = input("Enter Roll No: ")

    for student in students:
        if student["roll_no"] == roll_no:

            mark = student["mark"]

            if mark >= 50:
                result = "PASS"
            else:
                result = "FAIL"

            print("Name   :", student["name"])
            print("Mark   :", student["mark"])
            print("Result :", result)

            return

    print("Student not found.")


# Calculate Average
def calculate_average():
    print("\n--- AVERAGE MARK ---")

    if len(students) == 0:
        print("No students found.")
        return

    total = 0

    for student in students:
        total = total + student["mark"]

    average = total / len(students)

    print("Total Students :", len(students))
    print("Average Mark   :", round(average, 2))


# Highest Mark
def highest_mark():
    print("\n--- HIGHEST MARK ---")

    if len(students) == 0:
        print("No students found.")
        return

    highest = students[0]

    for student in students:
        if student["mark"] > highest["mark"]:
            highest = student

    print("Roll No :", highest["roll_no"])
    print("Name    :", highest["name"])
    print("Course  :", highest["course"])
    print("Mark    :", highest["mark"])


# Lowest Mark
def lowest_mark():
    print("\n--- LOWEST MARK ---")

    if len(students) == 0:
        print("No students found.")
        return

    lowest = students[0]

    for student in students:
        if student["mark"] < lowest["mark"]:
            lowest = student

    print("Roll No :", lowest["roll_no"])
    print("Name    :", lowest["name"])
    print("Course  :", lowest["course"])
    print("Mark    :", lowest["mark"])


# Count Students
def count_students():
    print("\n--- TOTAL STUDENTS ---")

    total = len(students)

    print("Total Students :", total)


# Search by Course
def search_by_course():
    print("\n--- SEARCH BY COURSE ---")

    course = input("Enter Course: ")

    found = False

    for student in students:
        if student["course"].lower() == course.lower():
            print("----------------------")
            print("Roll No :", student["roll_no"])
            print("Name    :", student["name"])
            print("Age     :", student["age"])
            print("Course  :", student["course"])
            print("Mark    :", student["mark"])

            found = True

    if not found:
        print("No students found for this course.")


# Search by Name
def search_by_name():
    print("\n--- SEARCH BY NAME ---")

    name = input("Enter Name: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("----------------------")
            print("Roll No :", student["roll_no"])
            print("Name    :", student["name"])
            print("Age     :", student["age"])
            print("Course  :", student["course"])
            print("Mark    :", student["mark"])

            found = True

    if not found:
        print("Student not found.")


# Sort Students by Mark
def sort_by_mark():
    print("\n--- STUDENTS SORTED BY MARK ---")

    sorted_students = sorted(
        students,
        key=lambda student: student["mark"],
        reverse=True
    )

    for student in sorted_students:
        print("----------------------")
        print("Roll No :", student["roll_no"])
        print("Name    :", student["name"])
        print("Course  :", student["course"])
        print("Mark    :", student["mark"])


# Sort Students by Name
def sort_by_name():
    print("\n--- STUDENTS SORTED BY NAME ---")

    sorted_students = sorted(
        students,
        key=lambda student: student["name"]
    )

    for student in sorted_students:
        print("----------------------")
        print("Roll No :", student["roll_no"])
        print("Name    :", student["name"])
        print("Course  :", student["course"])
        print("Mark    :", student["mark"])


# Student Report
def student_report():
    print("\n--- STUDENT REPORT ---")

    roll_no = input("Enter Roll No: ")

    for student in students:
        if student["roll_no"] == roll_no:

            mark = student["mark"]

            if mark >= 90:
                grade = "A+"
            elif mark >= 80:
                grade = "A"
            elif mark >= 70:
                grade = "B"
            elif mark >= 60:
                grade = "C"
            elif mark >= 50:
                grade = "D"
            else:
                grade = "F"

            if mark >= 50:
                result = "PASS"
            else:
                result = "FAIL"

            print("\n==============================")
            print("        STUDENT REPORT")
            print("==============================")
            print("Roll No :", student["roll_no"])
            print("Name    :", student["name"])
            print("Age     :", student["age"])
            print("Course  :", student["course"])
            print("Mark    :", student["mark"])
            print("Grade   :", grade)
            print("Result  :", result)
            print("==============================")

            return

    print("Student not found.")


# Attendance
def attendance():
    print("\n--- ATTENDANCE ---")

    roll_no = input("Enter Roll No: ")

    for student in students:
        if student["roll_no"] == roll_no:

            total = int(input("Enter Total Classes: "))
            attended = int(input("Enter Attended Classes: "))

            percentage = (attended / total) * 100

            print("\n--- ATTENDANCE DETAILS ---")
            print("Name       :", student["name"])
            print("Total      :", total)
            print("Attended   :", attended)
            print("Percentage :", round(percentage, 2), "%")

            if percentage >= 75:
                print("Status     : Eligible")
            else:
                print("Status     : Not Eligible")

            return

    print("Student not found.")


# Save Student Data
def save_data():
    with open("data.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Student data saved successfully!")


# Load Student Data
def load_data():
    global students

    try:
        with open("data.json", "r") as file:
            students = json.load(file)

        print("Student data loaded successfully!")

    except FileNotFoundError:
        print("No saved data found. Using default students.")


# Student Dashboard
def dashboard():
    print("\n==============================")
    print("       STUDENT DASHBOARD")
    print("==============================")

    if len(students) == 0:
        print("No students found.")
        return

    total = len(students)

    total_mark = 0
    highest = students[0]
    lowest = students[0]
    pass_count = 0
    fail_count = 0

    for student in students:

        total_mark = total_mark + student["mark"]

        if student["mark"] > highest["mark"]:
            highest = student

        if student["mark"] < lowest["mark"]:
            lowest = student

        if student["mark"] >= 50:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    average = total_mark / total

    print("Total Students :", total)
    print("Average Mark   :", round(average, 2))
    print("Highest Mark   :", highest["mark"])
    print("Highest Student:", highest["name"])
    print("Lowest Mark    :", lowest["mark"])
    print("Lowest Student :", lowest["name"])
    print("Pass Students  :", pass_count)
    print("Fail Students  :", fail_count)
    print("==============================")
def export_csv():
    import csv

    with open("students.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["roll_no", "name", "age", "course", "mark"]
        )

        writer.writeheader()
        writer.writerows(students)

    print("Student data exported to students.csv successfully!")
