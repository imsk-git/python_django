stu_names = ['Alice', 'Bob', 'Charlie']
avg_marks = [85, 92, 78]

stu_info = dict(zip(stu_names,avg_marks))
average = sum(avg_marks)/len(avg_marks)
print(f"{stu_info} and Average = {average}")

#Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78} and Average = 85.0



