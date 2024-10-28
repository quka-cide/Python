word = "Thank you"
user_word = input('What is your favorite letter? ')

for letter in word:
    if letter.lower() == user_word.lower():
      print("_", end="")
    else:
       print(letter.lower(), end="")
print()