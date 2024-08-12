#WAP to make a calculator.


num1 = input("Enter first digit: ")
if num1.replace('.','',1).isdigit():
    num1 = float(num1)
    operator = input("Enter operator(+,-,*,/): ")
    if operator in ['+','-','*','/']:
        num2 = input("Enter second digit: ")
        if num2.replace('.','',1).isdigit():
            num2 = float(num2)
            if operator=='+':
                print(num1, "+", num2, "=", num1+num2)
            elif operator=='-':
                print(num1, "-", num2, "=",num1-num2)
            elif operator=='*':
                print(num1, "*", num2, "=",num1*num2)
            elif operator=='/':
                if num2!=0:
                    print(num1, "/", num2, "=",num1/num2)
                else:
                    print("Can't divide by zero.")
        else:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice")
else:
    print("Invalid input. Please enter a number.")


#WAP to find input number is prime or composite

num = input("Enter number: ")
if num <= 1:
    pass


# num = float(input("Enter number: "))

# if num <= 1:
#     print("Number is neither prime nor composite.")
# elif num == 2:
#     print("Number is prime.")
# else:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("Number is prime.")
#     else:
#         print("Number is composite.")


