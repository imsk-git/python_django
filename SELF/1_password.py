import random
import string

class Password:
    def __init__(self,length, has_uppercase, has_numbers, has_special_chars) -> None:
        print("\nPassword Generator: \n-----------------------------------------")
        self.length = length
        self.has_uppercase = has_uppercase
        self.has_numbers = has_numbers
        self.has_special_chars = has_special_chars

    def password_generator(self):
        chars = string.ascii_lowercase
        if self.has_uppercase:
            chars += string.ascii_uppercase
        if self.has_numbers:
            chars += string.digits
        if self.has_special_chars:
            chars += string.punctuation

        password = [random.choice(chars) for _ in range(self.length)]

        # or
        # password = []
        # if self.has_uppercase:
        #     password.append(random.choice(string.ascii_uppercase))
        # if self.has_numbers:
        #     password.append(random.choice(string.digits))
        # if self.has_special_chars:
        #     password.append(random.choice(string.punctuation))
        # password.append(random.choice(string.ascii_lowercase))

        # for _ in range(self.length - len(password)):
        #     password.append(random.choice(chars))
        
        random.shuffle(password)
        return ''.join(password)

    def pw_generate(self):
        self.password = self.password_generator()
        print(f"\nGenerated Password: {self.password}\n\n************************************************")

def main():
    while True:
        length = input("\nEnter password length (min 8, max 128): ")
        if not length.isdigit():
            print("Invalid input. Please enter a number.")
        elif int(length) < 8:
            print("Password length must be at least 8 characters.")
        elif int(length) > 128:
            print("Password length must not exceed 128 characters.")
        else:
            length = int(length)
            break
            
    while True:
        has_uppercase = input("Include uppercase letters? (y/n): ").lower() 
        if has_uppercase not in ['y','n']:
            print("Invalid input. Please enter 'y' or 'n'. ")
        else:
            has_uppercase = (has_uppercase == 'y')
            break

    while True:
        has_numbers = input("Include numbers? (y/n): ").lower()
        if has_numbers not in ['y','n']:
            print("Invalid input. Please enter 'y' or 'n'. ")
        else:
            has_numbers = (has_numbers == 'y')
            break

    while True:
        has_special_chars = input("Include special charaters? (y/n): ").lower()
        if has_special_chars not in ['y','n']:
            print("Invalid input. Please enter 'y' or 'n'. ")
        else:
            has_special_chars = (has_special_chars == 'y')
            break

    password_obj = Password(length, has_uppercase, has_numbers, has_special_chars)
    password_obj.pw_generate()
main()

