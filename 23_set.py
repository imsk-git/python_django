data = ["apple", "ball", "apple","banana", "cat", "apple", "ball"]
data_set = set(data) #gives data in set and removes duplicate data
new_data = list(data_set) #again gives the data in list
print(new_data)


#it doesn't have indexing facility so output can't be same all the time and it's also fast then list
data_set = {1, 5, 9, 8}
data_set.add("apple")
print(data_set)