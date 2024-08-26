country_A = {"Nepal", "India", "Turkey"}
country_B = {"Turkey", "Spain"}
data = country_A | country_B
# or this method: data = country_A.union(country_B)
print(data)

#output: {'Turkey', 'India', 'Nepal', 'Spain'}



A = {1,2,9,7,6}
B = {5,8,3,9,4}
new_data = A & B
# or this method: new_data = A.intersection(B)
print(new_data) 

# output: 9