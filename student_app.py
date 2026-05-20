students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add new Student")
    print("2. Add branch")
    print("3. exit")
    

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print(f"{name} added successfully!")

    elif choice == "2":
        print("\nadd branch:")
        
        if len(branch) == 0:
            print("others")
        else:
            for branch in students:
                print(student)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
