student_data = []

def menu():
    print("\n -----------WELCOME TO THIS APPLICATION----------- \n")
    print("Enter 1 to register students.")
    print("Enter 2 to display list of students.")
    print("Enter 3 to search students.")
    print("Enter 4 to update students data.")
    print("Enter 5 to delete students data.")

def register_students():
    pid = len(student_data) + 1
    name = input("Enter students name: ").lower()
    age = input("Enter students age: ")
    address = input("Enter students address: ")
    class_no = input("Enter students class: ")
    roll_no = input("Enter students roll no.: ")
    student = {'pid':pid, 'name':name, 'age':age, 'address':address, 'class':class_no, 'roll_no':roll_no}
    student_data.append(student)
    print("Student registered successfully.")

def display():
    if not student_data:
        print("No Students Found.")
    else:
        for student in student_data:
            print(student)

def search():
    if not student_data:
        print("Students Data not Found.")
    else:
        search_name = input("Enter student's name to search: ")
        found = False
        for student in student_data:
            if student['name'] == search_name:
                print(student)
                found = True
        if not found:
            print("Student not Found.")

def update():
    if not student_data:
        print("Student's Data not Found.")
    else:
        update_name = input("Enter student's name to update data: ")
        found = False
        for student in student_data:
            if student['name'] == update_name:
                name = input("Enter students name: ")
                age = input("Enter students age: ")
                address = input("Enter students address: ")
                class_no = input("Enter students class: ")
                roll_no = input("Enter students roll no.: ")
                student['name'] = name
                student['age'] = age
                student['address'] = address
                student['class_no'] = class_no
                student['roll_no'] = roll_no
                print("Student's data updated successfully.")
                found = True
        if not found:
            print("ID not Found.")

def delete():
    if not student_data:
        print("Student's Data not Found.")
    else:
        delete_pid = int(input("Enter student's ID to delete data: "))
        found = False
        for student in student_data:
            if student['pid'] == delete_pid:
                student_data.remove(student)
                found = True
                print("Student's Data deleted successfully.")
        if not found:
            print("Student's ID not Found.")

def main():
    while True:
        menu()
        input_option = input("Enter your choice: ")
        if input_option == '1':
            register_students()

        elif input_option == '2':
            display()

        elif input_option == '3':
            search()

        elif input_option == '4':
            update()

        elif input_option == '5':
            delete()
            
        else:
            print("Invalid input. Please try again.")

        while True:
            exit = input("Do you want to exit? y/n: ").lower()
            if exit == 'y':
                print("Exiting the program. GoodBye! ")
                return
            elif exit == 'n':
                break
            else:
                print("Invalid input. Please enter y/n.")
main()
