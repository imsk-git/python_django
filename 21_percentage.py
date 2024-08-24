#WAP to ask subject and their marks and print their percentage and division

# num_subjects = int(input("Enter the number of subjects: "))
# total_marks = 100
# marks = []
# for i in range(num_subjects):
#     subject = input(f"Enter {i + 1} subject name: ")
#     while True:
#         marks_sub = int(input(f"Enter marks for subject {subject}: "))
#         if marks_sub.isdigit() and 0 <= marks_sub <= total_marks:
   
#             marks.append(marks_sub)
#             break
#         else:
#             print("Invalid input. Please enter numeric value.")
# percentage = (sum(marks) / (num_subjects * total_marks)) * 100
# average_marks = sum(marks) / len(marks)
# print(f"Marks Percentage: {percentage:.2f}%")
# print(f"Average Marks: {average_marks:.2f}")
# if percentage >= 85:
#     print("Distinction")
# elif percentage >= 70:
#     print("First Division")
# elif percentage >= 65:
#     print("Second Division")
# elif percentage >= 40:
#     print("Third Division")
# else:
#     print("Fail")



total_students = []
for student in range(0,2):
    no_of_subject = int(input("Enter no. of subject: "))
    subject_mark ={}
    marks_obtained = 0
    total_marks = no_of_subject*100
    student_name = input(f"Enter student {student + 1} name: ")
    for i in range(no_of_subject):
        subject = input(f"Enter {i + 1} subject name: ")
        mark = int(input(f"Enter {subject} marks: "))
        subject_mark[subject] = mark
        marks_obtained = marks_obtained + mark
    percentage = round((marks_obtained/total_marks) *100,2)
    if percentage >= 85:
        division = "Distinction"
    elif percentage >= 70:
        division = "First Division"
    elif percentage >= 65:
        division = "Second Division"
    elif percentage >= 40:
        division = "Third Division"
    else:
        division = "Fail"
    subject_mark['student_name'] = student_name
    subject_mark['percentage'] = percentage
    subject_mark['division'] = division
    total_students.append(subject_mark)
print("Your data is: ",total_students)





