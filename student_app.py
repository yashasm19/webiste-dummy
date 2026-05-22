students = []

while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Add Branch")
    print("3. Add Phone Number")
    print("4. View Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    # ADD STUDENT
    if choice == "1":

        name = input("Enter student name: ")

        student = {
            "name": name,
            "branch": "",
            "phone": ""
        }

        students.append(student)

        print(f"{name} added successfully!")

    # ADD BRANCH
    elif choice == "2":

        student_name = input("Enter student name to add branch: ")

        found = False

        for student in students:

            if student["name"] == student_name:

                branch = input("Enter branch: ")

                student["branch"] = branch

                print("Branch updated successfully!")

                found = True

        if found == False:
            print("Student not found")

    # ADD PHONE NUMBER
    elif choice == "3":

        student_name = input("Enter student name to add phone number: ")

        found = False

        for student in students:

            if student["name"] == student_name:

                phone = input("Enter phone number: ")

                student["phone"] = phone

                print("Phone number updated successfully!")

                found = True

        if found == False:
            print("Student not found")

    # VIEW STUDENTS
    elif choice == "4":

        print("\n--- Student Details ---")

        if len(students) == 0:

            print("No students found")

        else:

            for student in students:

                print(f"\nName : {student['name']}")

                if student['branch'] != "":
                    print(f"Branch : {student['branch']}")

                if student['phone'] != "":
                    print(f"Phone : {student['phone']}")

    # EXIT
    elif choice == "5":

        print("Exiting program...")
        break

    # INVALID OPTION
    else:

        print("Invalid choice")