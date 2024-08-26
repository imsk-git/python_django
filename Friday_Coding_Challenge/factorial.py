num = int(input("Enter any number to print factorial: "))
result = 1
for i in range(1, num + 1):
    result *= i
print(f"Factorial of {num} is {result}")

#output: Factorial of 8 is 40320 