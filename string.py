name = "ram is  a student"
print (name.upper())
print (name.lower())
print (name.title())
print (name.capitalize())
print (name.swapcase()) #changes lowercase to upper and vice versa
print (name.strip()) #removes white space


split_data = name.split(' ')
print(split_data)


email = "ram@gmail.com"
split_data = email.split('@')
print(split_data)
print(split_data[0])