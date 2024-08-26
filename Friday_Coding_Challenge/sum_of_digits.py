# num = (input("Enter numbers to calculate sum: "))
# for digit in str(num):
#     sum_of_digit = sum(str(digit))
# print(f"The sum of {num} is {sum_of_digit}")



numbers = input("Enter any number to calculate sum: ")
num = sum(int(number) for number in numbers)
print(f"The sum of {numbers} is {num}.")

#output; The sum of 1234 is 10.