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








