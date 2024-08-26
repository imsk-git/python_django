word = input("Enter any word to check whether the entered word is palindrome or not: ")
reversed_word = word[::-1]
if word == reversed_word:
    print(f"{word} is Palindrome.")
else:
    print(f"{word} is not Palindrome.")

#output: 12321 is Palindrome
#output: 123456 is not Palindrome
#output: madam is Palindrome
#output: hate is not Palindrome
