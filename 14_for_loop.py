sum = 0
data = "123456"
for i in data:
    num = int(i)
    sum = num + sum
print(f"Sum of {data} is:", sum )



# WAP to find highest number


data = "822457313496"
highest_number = 0
for i in data:
    number = int(i)
    if highest_number<number:
        highest_number=number
print(f"Highest number in {data} is:",highest_number)



data = "8547932158756982145"
lowest_number = 5
for i in data:
    number = int(i)
    if lowest_number>number:
        lowest_number = number
print(f"Lowest number in {data} is: ",lowest_number)
