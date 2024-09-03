num1 = int(input("Enter first number: "))
operator = input("Enter operator(+, -, *, /): ")
num2 = int(input("Enter second number: "))

class Calculator:
    def add(self,num1,num2):
        return num1 + num2
    def substract(self,num1,num2):
        return num1 - num2
    def multiply(self,num1,num2):
        return num1 * num2
    def divide(self,num1,num2):
        if num2 == 0:
            print("Zero is not divisible.")
            return None
        return num1 / num2

def calculate(num1, operator, num2):
    obj = Calculator()
    if operator == '+':
        print(obj.add(num1,num2))
    elif operator == '-':
        print(obj.substract(num1,num2))
    elif operator == '*':
        print(obj.multiply(num1,num2))
    elif operator == '/':
        result = obj.divide(num1,num2)
        if result is not None:
            print(round(result,2))
    else:
        print("Invalid Operator.")


calculate(num1, operator, num2)