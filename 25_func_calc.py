# #parameter with return type
# def calculator(num_1, operator, num_2):
#     if '+' in operator: 
#         return num_1 + num_2
#     elif '-' in operator: 
#         return num_1 - num_2
#     elif '*' in operator: 
#         return num_1 * num_2
#     elif '/' in operator: 
#         if num_2 != 0:
#             return num_1 / num_2
#         else:
#             print("Zero is not divisible.")
#     else:
#         return "Invalid input. Please enter from (+, -, *, /) only."
# num_1 = int(input("Enter 1st number: "))
# operator = input("Enter operator(+, -, *, /): ")
# num_2 = int(input("Enter 2nd number: "))
# print(calculator(num_1, operator, num_2))
# print("*************************************************************")




# #no parameter with return type
# def calculator():
#     num_1 = int(input("Enter 1st number: "))
#     operator = input("Enter operator(+, -, *, /): ")
#     num_2 = int(input("Enter 2nd number: "))
#     if '+' in operator: 
#         return num_1 + num_2
#     elif '-' in operator: 
#         return num_1 - num_2
#     elif '*' in operator: 
#         return num_1 * num_2
#     elif '/' in operator: 
#         if num_2 != 0:
#             return num_1 / num_2
#         else:
#             print("Zero is not divisible.")
#     else:
#         return "Invalid input. Please enter from (+, -, *, /) only."
# calculator()
# print("*************************************************************")




# #parameter with no return type 
# def calculator(num_1, operator, num_2):
#     if '+' in operator: 
#         print(num_1 + num_2)
#     elif '-' in operator: 
#         print(num_1 - num_2)
#     elif '*' in operator: 
#         print(num_1 * num_2)
#     elif '/' in operator: 
#         if num_2 != 0:
#             print(num_1 / num_2)
#         else:
#             print("Zero is not divisible.")
#     else:
#         print("Invalid input. Please enter from (+, -, *, /) only.")
# num_1 = int(input("Enter 1st number: "))
# operator = input("Enter operator(+, -, *, /): ")
# num_2 = int(input("Enter 2nd number: "))
# calculator(num_1, operator, num_2)
# print("*************************************************************")






# parameter with no return type
# def add(num1,num2):
#     print(num1+num2)
# def substract(num1,num2):
#     print(num1-num2)
# def multiply(num1,num2):
#     print(num1*num2)
# def divide(num1,num2):
#     if num2 != 0:
#         print(num1 / num2)
#     else:
#         print("Zero is not divisible.")
# num1 = int(input("Enter 1st number: "))
# operator = input("Enter operator(+, -, *, /): ")
# num2 = int(input("Enter 2nd number: "))
# if operator == '+':
#     add(num1,num2)
# elif operator == '+':
#     substract(num1,num2)
# elif operator == '+':
#     multiply(num1,num2)
# elif operator == '+':
#     divide(num1,num2)



def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Zero is not divisible. ")

def calculator():
    while True:
        num1 = int(input("Enter first number: "))
        operator = input("Enter operator(+, -, *, /): ")
        num2 = int(input("Enter second number: "))
        if operator == '+':
            result = add(num1, num2)
            print(f"The sum of {num1} and {num2} is {result}")
        elif operator == '-':
            result = substract(num1, num2)
            print(f"The difference between {num1} and {num2} is {result}")
        elif operator == '*':
            result = multiply(num1, num2)
            print(f"The product of {num1} and {num2} is {result}")
        elif operator == '/':
            result = division(num1, num2)
            print(f"The division of {num1} and {num2} is {result}")
        else:
            print("Invalid operator. Please enter from (+, -, *, /) only.")

        while True:
            exit_option = input("Do you want to exit? y/n: ").lower()
            if exit_option == 'y':
                print("Exiting the program. Goodbye!")
                return
            elif exit_option == 'n':
                break
            else:
                print("Invalid input. Please enter y/n.")
calculator()



