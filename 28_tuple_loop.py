first_tuple = ("mathema","python","c++")
list_data = []
for first in first_tuple:
    added = first + "tics"
    list_data.append(added)
    new_data = tuple(list_data)
print(new_data)