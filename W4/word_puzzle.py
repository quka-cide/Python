# Added a limitations to the number of guesses. When the user has made 6 guesses, it's said that the game is over.
secret_word = 'mosiah'

print('Welcome to the word guessing game!')
print()

guess_count = 0

hint = '_ ' * len(secret_word)

print(f'Your hint is: {hint}')

while True:
    if guess_count == 6:
        print("Game over. you've used every attempt")
        break

    guess_word = input('What is your guess? ').lower()

    guess_count += 1

    if len(guess_word) != len(secret_word):
        print('Sorry, the guess must have the same number of letters as the secret word.')
    else:
        hint = ''
        for i in range(len(secret_word)):
            if guess_word[i] == secret_word[i]:
                hint += guess_word[i].upper()
            elif guess_word[i] in secret_word:
                hint += guess_word[i].lower()
            else:
                hint += '_ '
    

    if guess_word.lower() == secret_word:
        print('Congratulations! You guessed it!')
        print(f'It took you {guess_count} guesses.')
        break
    else:
        print('Your guess was not correct.')

    print(f'your hint is: {hint}')
