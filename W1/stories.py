# I added 1 sentence at the end. I also added some new variables.
# It now includes the option to add "a" or "an" before certain words based on the following word's initial letter.
print('Please enter the following:')

adjective = input('adjective: ')
animal = input('animal: ')
verb_1 = input('verb: ')
exclamation = input('exclamation: ')
verb_2 = input('verb: ')
verb_3 = input('verb: ')
# new variables 
noun = input('noun: ')
place = input('place: ')
verb_4 = input('verb: ')
adjective_2 = input('adjective: ')

a_or_an = 'a'
if noun[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    a_or_an = 'an'

print('\nYour story is:')
print()
print(f'The other day, I was really in trouble. It all started when I saw a very\n'
f'{adjective} {animal} {verb_1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all\n'
f'I could think to do was to {verb_2} over and over. Miraculously,\n'
f'that caused it to stop, but not before it tried to {verb_3}\nright in front of my family.\n'
f'I quickly grabbed {a_or_an} {noun} and ran to {place} to {verb_4} it. It was {adjective_2}!\n')