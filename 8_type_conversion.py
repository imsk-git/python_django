value = 'a'
print("Before conversion: ",type(value))
value_num = str(value)
print("After conversion: ",type(value_num))

#WAP to take user input mark percentage and find their division

percentage = input("Enter your mark percentage: ")
per = int(percentage)
if per<40:
    print("NA")
elif (40<=per<55):
    print("Third Division")
elif(55<=per<75):
    print("Second Division")
elif(75<=per<85):
    print("First Division")
else:
    print("Distinction")


