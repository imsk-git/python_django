words = input("Enter anything to reverse the order: ")
reverse_words = words[::-1]
print(f"The reverse of {words} is {reverse_words}")

#next method
words = input("Enter anything to reverse the order: ")
reverse_words = ''.join(reversed(words))
print(f"The reverse of {words} is {reverse_words}")

#output: The reverse of Python is nohtyp