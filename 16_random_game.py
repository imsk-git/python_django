#WAP to create a random game and give limited attempts to guess.

import random
random_number = random.randrange(1,100)

# a = 1
# while a <= 5:
#     a += 1
#     guess_number = int(input("Guess any number: "))
#     if guess_number == random_number:
#         print("Congratulations! Your guess is correct.")
#         break
#     elif guess_number < random_number:
#         print("Your guess is lesser than random number.")
#     else:
#         print("Your guess is greater than random number.")
# else:
#     print("You've exceeded the maximum number of attempts. The correct answer was: ",random_number)
    

#WAP to create a random game and give limitless attempts to guess and score according to their no. of attempts to guess.

print("\n Welcome to the limitless number guessing game.\n")
attempts = 0
while True:
    attempts += 1
    guess_number = int(input("Guess any number: "))
    if guess_number == random_number:
        # score += 1
        print("Congratulations! Your guess was correct")
        break
    elif guess_number > random_number:
        # score -= 1
        print("Your guess is greater than random number.")
    else:
        # score -= 1
        print("Your guess is lesser than the random number.")
print(f"""You scored {10 - attempts}""")


