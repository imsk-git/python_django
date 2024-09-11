
#Overriding
class Animal:
    def sound(self):
        print("This is animal sound.")

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def sound(self):
        print("Bark")

obj = Dog()
obj.sound() #It only prints Bark b'coz its overriding the method "sound"


a = 10
b = 15
class Mathematics:
    def add(self,a,b):
        print(f"Addition: {a+b}")

    def sub(self,a,b):
        print(f"Substraction: {a - b}")

    def product(self,a,b,c =5):
        print(f"Multiplication: {a * b - c}")

class Override(Mathematics):
    def add(self,a,b):
        super().add(a,b)

    def sub(self,a,b):
        super().sub(a,b)

    def product(self,a,b,c =5):
        super().product(a,b,c)

math_obj = Override()
math_obj.add(a,b)
math_obj.sub(a,b)
math_obj.product(a,b)