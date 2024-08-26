vowels = "aeiouAEIOU" 
word = input("Enter any word: ")
vowel_count = 0
for char in word:
    if char in vowels:
        vowel_count += 1
print(f"'{word}' has {vowel_count} vowels.")

# output :Enter any word: hello world pythOn djAngO
#         'hello world pythOn djAngO' has 6 vowels.


# vowels = "aeiouAEIOU"
# word = input("Enter any word: ")
# vowel_count = sum(1 for char in word if char in vowels)
# print(f"The word '{word}' contains {vowel_count} vowels.")