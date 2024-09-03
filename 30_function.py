def convert(first_args):
    print(type(first_args))
    data = int(first_args)
    print(type(data))
    return data

def odd_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
number = input("Enter number: ")
output = convert(number)
odd_even_output = odd_even(output)

if odd_even_output == True:
    print("It's Even.")
else:
    print("It's Odd.")


# output:
# Enter number: 5
# <class 'str'>
# <class 'int'>
# It's Odd.