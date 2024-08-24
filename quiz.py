while True:
    is_quiz = input("Do you want to take the quiz, y/n?")
    if is_quiz == 'n':
        break
    elif is_quiz == 'y':
        score = 0
        ques1 = input("""Who invented Python?
                      Choices:
                      1. A
                      2. B
                      3. C""")
        ans1 = input("Enter your answer (1 , 2 , 3): ")
        if ans1 == '1':
            score += 1
            print("Correct")
        else:
            print("Incorrect. The correct answer is 1.")
        ques2 = input("""Who invented Java?
                      Choices:
                      1. A
                      2. B
                      3. C""")
        ans2 = input("Enter your answer (1 , 2 , 3): ")
        if ans2 == '3':
            score += 1
            print("Correct")
        else:
            print("Incorrect. The correct answer is 3.")
        ques3 = input("""Who invented Javascript?
                      Choices:
                      1. A
                      2. B
                      3. C""")
        ans3 = input("Enter your answer (1 , 2 , 3): ")
        if ans3 == '2':
            score += 1
            print("Correct")
        else:
            print("Incorrect. The correct answer is 2.")
        print(f"Your final score is {score} out of 3.")

    else:
        print("Please enter y/n.")





# WAP to input 10 numbers and print average of the sum 
sum = 0
for i in range(10):
    num = int(input(f"Enter {i+1} number: "))
    sum += num
print(f"The average of {sum} is: {sum/10}")




# WAP to play rock, paper, scissors with computer
while True:
    is_play = input("Do you want to play rock-paper-scissors, y/n? ")
    if is_play == 'n':
        break
    elif is_play == 'y':
        while True:
            user_choice = input("Enter your choice (rock, paper, scissors): ")
            if user_choice in ['rock','paper','scissors']:
                break
            else:
                print("Invalid input. Please enter rock, paper or scissors.")
        import random
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        if user_choice == computer_choice:
            print("YAY! You are the winner")
        else:
            print(f"Sorry! Hope to match in next move. The right choice was {computer_choice}")
    else:
        print("Please enter y/n.")    