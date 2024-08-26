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







def add(num1,num2):
    print(num1+num2)
def substract(num1,num2):
    print(num1-num2)
def multiply(num1,num2):
    print(num1*num2)
def divide(num1,num2):
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Zero is not divisible.")
num1 = int(input("Enter 1st number: "))
operator = input("Enter operator(+, -, *, /): ")
num2 = int(input("Enter 2nd number: "))
if operator == '+':
    add(num1,num2)
elif operator == '+':
    substract(num1,num2)
elif operator == '+':
    multiply(num1,num2)
elif operator == '+':
    divide(num1,num2)
