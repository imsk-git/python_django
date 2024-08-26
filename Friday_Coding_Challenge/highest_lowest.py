#1st method
highest_number = 0
lowest_number = 0
numbers = "0124392566"
for number in numbers:
    num = int(number)
    if num > highest_number:
        highest_number = num
    if num < lowest_number:
        lowest_number = num
print(f"Highest Number: {highest_number}")
print(f"Lowest Number: {lowest_number}")




#2nd method 
number = "0124392566"
number = [int(num) for num in numbers]
print(f"Highest Number: {max(number)}")
print(f"Lowest Number: {min(number)}")

#output: Highest Number: 9
#        Lowest Number: 0