num = int(input("Enter number: "))
numbers = range(1,num+1)
n = ', '.join(str(num**2) for num in numbers)
print(n)

#output: Enter number: 7
#        1, 4, 9, 16, 25, 36, 49
