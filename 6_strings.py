# name = "ram is  a student"
# print (name.upper())
# print (name.lower())
# print (name.title())
# print (name.capitalize())
# print (name.swapcase()) #changes lowercase to upper and vice versa
# print (name.strip()) #removes white space


# split_data = name.split(' ')
# print(split_data)


email = "ram@gmail.com"
split_data = email.replace('@','.').split('.')
print(split_data)
print(split_data[0])


# WAP to make 10 examples of string manipulation

name = "   shYam Is a taxI   drivEr."
print (name.upper())  #    SHYAM IS A TAXI DRIVER.
print (name.isupper()) #False
print (name.lower()) #   shyam is a taxi driver.
print (name.title()) #   Shyam Is A Taxi Driver.
print (name.swapcase()) #   SHyAM iS A TAXi DRIVeR.
print(name.capitalize()) #   shyam is a taxi driver.
print(name.casefold()) #   shyam is a taxi driver.
print (name.strip()) #shYam Is a taxI drivEr.
print (name.encode()) #b'   shYam Is a taxI drivEr.'
print (name.rsplit()) #['shYam', 'Is', 'a', 'taxI', 'drivEr.']
print (name.rstrip('taxI')) #   shYam Is a taxI drivEr.
print(name.center(5,'!')) #   shYam Is a taxI drivEr.
print(name.replace('shYam','raM')) #  raM Is a taxI drivEr.


data = "I love veg food."
print(data.replace('veg','non-veg'))