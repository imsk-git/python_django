
# to add data in tuple by using another data type beacause tuple is immutable.
first_tuple = (4,6,7,2,5)
new_data = list(first_tuple)
new_data.append(5)
data = tuple(new_data)
print(data)