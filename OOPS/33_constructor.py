class Mathematics:
    def __init__(self, first_number, second_number) -> None:
        self.a = first_number
        self.b = second_number
        self.sum()
        self.difference()
        self.multiply()
    def sum(self):
        print("Addition is: ",self.a + self.b)
    def difference(self):
        print("Substraction is: ",self.a - self.b)
    def multiply(self):
        print("Substraction is: ",self.a * self.b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

obj = Mathematics(a,b)
