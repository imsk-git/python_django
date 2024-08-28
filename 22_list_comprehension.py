items = [1,2,3,4,5,6,7,8,9,10]

# #without using list comprehension
# list = []
# for item in items:
#     list.append(item*item)
# print(list)



# #using list compresion for cube numbers
# list = [item**3 for item in items]
# print(list)


#without using list comprehension adding 1000 to items
list = []
for item in items:
    list.append(item+1000)
print(list)


#with using list comprehension adding 1000 to items
list = [item+1000 for item in items]
print(list)

list = []
for item in items:
    if item % 2 == 0:
        list.append(item)
    else:
        pass


print("Even numbers are: ",list)
print("Odd numbers are: ",list)


data = ["apple", "ball", "cat", "dog", "ball", "cat"]
new_list = []
for item in data:
    if item in new_list:
        pass
    else:
        new_list.append(item)
print(data)


number = input("Enter the number: ")
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")






