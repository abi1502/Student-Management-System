from student import (
    students,
    add_student,
    display_students,
    search_student,
    update_student,
    delete_student,
    calculate_grade,
    pass_fail,
    calculate_average,
    highest_mark,
    lowest_mark,
    count_students,
    search_by_course,
    search_by_name,
    sort_by_mark,
    sort_by_name,
    student_report,
    attendance,
    save_data,
    load_data,
    dashboard,
    export_csv
)


print("================================================================================")
print("                      STUDENT MANAGEMENT SYSTEM")
print("================================================================================")


# Load saved data
load_data()


# Student Dashboard Menu
while True:

    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Grade")
    print("7. Pass / Fail")
    print("8. Average Mark")
    print("9. Highest Mark")
    print("10. Lowest Mark")
    print("11. Count Students")
    print("12. Search by Course")
    print("13. Search by Name")
    print("14. Sort by Mark")
    print("15. Sort by Name")
    print("16. Student Report")
    print("17. Attendance")
    print("18. Save Data")
    print("19. Student Dashboard")
    print("20. Export to CSV")
    print("21. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_grade()

    elif choice == "7":
        pass_fail()

    elif choice == "8":
        calculate_average()

    elif choice == "9":
        highest_mark()

    elif choice == "10":
        lowest_mark()

    elif choice == "11":
        count_students()

    elif choice == "12":
        search_by_course()

    elif choice == "13":
        search_by_name()

    elif choice == "14":
        sort_by_mark()

    elif choice == "15":
        sort_by_name()

    elif choice == "16":
        student_report()

    elif choice == "17":
        attendance()

    elif choice == "18":
        save_data()

    elif choice == "19":
        dashboard()

    elif choice == "20":
        export_csv()

    elif choice == "21":
        save_data()
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
