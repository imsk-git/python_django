data = "I'm veg"

if "veg" in data:
    print("You can eat vegetables.")
else:
    print("You can eat meat.")

data = "I'm vegeterian"

if "veg" in data:
    print("You can eat vegetables.")
else:
    print("You can eat meat.")

data = "I'm good"

if "veg" in data:
    print("You can eat vegetables.")
else:
    print("You are fine.")


#WAP to take user input email and validate wether it is correct email or not
email = input("Enter your email: ")
if '@' and '.com' in email:
    print(email,"is valid")
else:
    print("This" ,email, "email is invalid")

# email validation using not in
email = input("Enter your email: ")
if '@' and '.com' not in email:
    print("This" ,email, "email is invalid")
else:
    print(email,"is valid")





