# WAP to make a calculator, firstly ask user if wants to calculate : if presses y then calculation is procced otherwise if n is pressed then then terminate the calculator with the help of break

while True:
    is_play = input("Do you want to calculate, y/n?")
    if is_play == 'n':
        break
    elif is_play == 'y':
        num1 = input("Enter 1st number: ")
        if num1.replace('.','',1).isdigit():
            num1 = float(num1)
            operator = input("Enter operator (+ , - , * , /): ")
            num2 = input("Enter 2nd number: ")
            if num2.replace('.','',1).isdigit():
                num2 = float(num2)
                if operator == '+':
                    print(num1+num2)
                elif operator == '-':
                    print(num1-num2)
                elif operator == '*':
                    print(num1*num2)
                elif operator == '/':
                    if num2 != 0:
                        print(num1/num2)
                    else:
                        print("Zero is not divisible.")
                else:
                    print("Invalid operator. Please enter among (+ , - , * , /): ")
            else:
                print("Enter (0-9) in 2nd number.")
        else:
            print("Enter (0-9) in 1st number.")
    else:
        print("Please enter y/n.")



#WAP to take 5 input number and find sum of all

# sum = 0
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# num3 = int(input("Enter 3rd number: "))
# num4 = int(input("Enter 4th number: "))
# num5 = int(input("Enter 5th number: "))
# data = num1 + num2 + num3 + num4 + num5
# print(f"The sum of all numbers is:",data)


sum = 0
for i in range(5):
    sum += int(input(f"Enter {i+1} number: "))
print(f"The sum of all numbers is: {sum}")






    

