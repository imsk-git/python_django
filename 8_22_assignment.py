# zip, enumerate, list_compression

# create list
# append data to list and print
# how to access and change value of list

country_list = ['Nepal','India','Pakistan','China']
country_list.append('Japan')
country_list[3] = 'Qatar'
print(country_list)




# create dict
# append data to dict and print
# how to access and change value of dict

my_dict = {'name':'Shreya', 'address': 'KTM', 'course':'Python'}
my_dict.update({'contact':'123456789'}) #to add data
my_dict['email'] = 'abc@gmail.com' #also to add data
my_dict['name'] = 'Sweta' #to chnage data
print(my_dict) #to print all the data
print(my_dict['email']) #prints only specified value of the given key 




# add dict to list
# print mark and student_name using loop from data = [{'name':"salman",'percentage':45},{'name':"mithun",'percentage':45}]

total_students = []
for student in range(0,2):
    student_name = input(f"Enter {student + 1} student name: ")
    no_of_subject = int(input("Enter No. of Subjects mark to print of Students: "))
    obtained_marks = 0
    total_number = no_of_subject * 100
    subject_marks = {}
    for subject in range(no_of_subject):
        subject = input(f"Enter {subject + 1} subject name: ")
        mark = int(input(f"Enter marks for {subject} subject: "))
        obtained_marks += mark
        subject_marks[subject] = mark
        percentage = round((obtained_marks/total_number) * 100, 2)
    subject_marks['percentage'] = percentage
    total_students.append(subject_marks)
print(f"Your data is: {total_students}")


