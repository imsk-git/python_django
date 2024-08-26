month = "October","November"

month_list = [month,"December","4587",147] #or
# month_list = ((month,"January")) #both are list
print(month_list) #[('October', 'November'), 'December', '4587', 147]
print(month_list[0]) #0th position output #('October', 'November')
print(month_list[-1]) #prints from last #147
# print(month_list[start:end:step])
print(month_list[0:3:2]) #[('October', 'November'), '4587']
print(month_list[::]) #[('October', 'November'), 'December', '4587', 147]
print(month_list[4:0:-1]) #[147, '4587', 'December']


month_list.append("March") #append helps to add some data in list
print(month_list) #[('October', 'November'), 'December', '4587', 147, 'March']

month_list.insert(0,"September") # insert helps to add data in specified position in list
print(month_list) #['September', ('October', 'November'), 'December', '4587', 147, 'March']


month_list.pop(0) #removes according to position in list
month_list.pop() #removes last item from the list

month_list.remove("December") #removes data from list
month_list.clear() #empty the list

print(len(month_list)) #gives length of list  #ans is 4


month_list[0] = "Mangsir" #helps to replace data
print(month_list) #['Mangsir', '4587', 147, 'March']





#WAP to find highest number in [1,5,9,6,89,1203,4,23]

highest_number = [1,5,9,6,89,1203,4,23]
print (max(highest_number)) #1203


# highest_number.sort() #to sort
# print(highest_number) #[1, 4, 5, 6, 9, 23, 89, 1203]

#compare and sort

sort_list = []
for number in highest_number:
    if not sort_list or number > sort_list[-1]:
        sort_list.append(number)
    else:
        for i in range(len(sort_list)):
            if number <= sort_list[i]:
                sort_list.insert(i,number)
                break
print(sort_list)

#swap the numbers 
a = 50
b = 78
print("Before swapping: ",a,b)
temp = a
a = b
b = temp
print("After swapping: ",a,b)



