class Employee:
    def __init__(self,name,current_salary) -> None:
        self.name = name
        self.current_salary = current_salary
        print(f"\n{self.name}'s current salary: {self.current_salary}")
        self.bonus()
        self.tax()

    def bonus(self):
        bonus = 5000
        self.bonus_with_salary = bonus
        print(f"{self.name}'s salary after adding bonus: {self.bonus_with_salary} ")

    def tax(self):
        tax = 13
        self.tax_with_salary = tax/100 * self.current_salary
        print(f"{self.name}'s salary after deducting tax: {self.tax_with_salary}")
    
    def total_salary(self):
        self.total_salary = self.current_salary + self.bonus_with_salary - self.tax_with_salary
        print(f"Total Salary: {self.total_salary} \n")

name = input("Enter your name: ")
salary = int(input("Enter your salary: "))

ram_obj = Employee(name, salary)
ram_obj.total_salary()

