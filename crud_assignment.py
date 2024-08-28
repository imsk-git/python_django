#WAp to make crud application for school having search option name, address,class, roll no., list of students, pid, 

student_data = []
pid = 1
    
while True:
    print("\n ******************Welcome********************* \n")
    print("Select 1 to register new students.")
    print("Select 2 to display all students list.")
    print("Select 3 to search students name.")
    print("Select 4 to update student's list.")
    print("Select 5 to delete student's list.")
    print("Do you want to exit. y/n? ")
    input_option = input("")
    if input_option == 'y':
        break
    elif input_option == 'n':
        input_option = input("Enter your option: ")
        if input_option == '1':
            name = input("Enter student name: ")
            age = input("Enter your age: ")
            address = input("Enter address: ")
            class_no = input("Enter your class: ")
            roll_no = input("Enter roll no.: ")
            student_data.append({'pid':pid, 'name':name, 'age':age,'address':address, 'class_no':class_no, 'roll_no':roll_no})
            # if student_data
            pid += 1
            print("Data added succesfully. ")
        elif input_option == '2':
            if not student_data:
                 print("No students registered. ")
            else:
                print("Registered Student's List: ")
                for i, student in enumerate(student_data, start = 1):
                    print(f"Student {i}: ")
                    print(f"PID: {student['pid']}")
                    print(f"Name: {student['name']}")
                    print(f"Age: {student['age']}")
                    print(f"Address: {student['address']}")
                    print(f"Class: {student['class_no']}")
                    print(f"Roll No.: {student['roll_no']}")
                    print("---------------------")
        elif input_option == '3':
            search_name = input("Enter student name to search: ")
            found = False
            for student in student_data:
                if student['name'] == search_name:
                    print(f"PID: {student['pid']}")
                    print(f"Name: {student['name']}")
                    print(f"Age: {student['age']}")
                    print(f"Address: {student['address']}")
                    print(f"Class: {student['class_no']}")
                    print(f"Roll No.: {student['roll_no']}")
                    found = True
                    break
            if not found:
                    print("Student not found.")
        elif input_option == '4':
            pass
        elif input_option == '5':
            pass
        else:
            print("Invalid Option. Please try again.")
    else:
            print("Invalid Option. Please try again.")
    
         



