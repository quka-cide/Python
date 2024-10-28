# Playtested the game with two friends. They enjoyed the interactive story and found the choices engaging. One suggested adding more descriptive language to enhance the atmosphere.

print('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?')
choice1 = input().lower()

if choice1 == 'match':
    print('You pick up the match and strike it, illuminating the area briefly. In that moment, you see a large grizzly bear not too far away. The match burns out quickly.')
    print('Do you want to RUN or HIDE behind a tree?')
    choice2 = input().lower()

    if choice2 == 'run':
        print("You sprint as fast as you can, the bear's heavy footsteps getting closer behind you. Suddenly, you encounter a fallen tree blocking your path.")
        print('Do you want to JUMP over it, or try to GO AROUND it? ')
        choice3 = input().lower()

        if choice3 == 'jump':
            print('You muster all your strength and leap over the fallen tree, landing safely on the other side. You continue running until you reach the edge of the forest. You have escaped the bear!')
        elif choice3 == 'go around':
            print('You try to go around the fallen tree, but it takes too long. The bear catches up to you, and you are unable to escape. Game over.')
        else:
            print('Invalid choice. Please try again.')

    elif choice2 == 'hide':
        print('You quickly duck behind a nearby tree, holding your breath as the bear approaches. After it passes, you cautiously step out.')
        print('Do you want to CONTINUE down the path, or GO BACK to where you found the match and flashlight?')
        choice3 = input().lower()

        if choice3 == 'continue':
            print('You walk down the path, eventually finding your way out of the forest. You have successfully avoided the bear!')
        elif choice3 == 'go back':
            print('You decide to go back, but you get lost in the darkness. The bear finds you, and you are unable to escape. Game over.')
        else:
            print('Invalid choice. Please try again.')
    else:
        print('Invalid choice. Please try again.')

elif choice1 == 'flashlight':
    print('You pick up the flashlight and turn it on, illuminating the path ahead. However, you also hear a noise off to the side.')
    print('Do you want to FOLLOW the path or LOOK in the trees for the source of the noise?')
    choice2 = input().lower()

    if choice2 == 'follow':
        print('You follow the path, hoping it will lead you to safety. The noise grows louder, and you shine your light into the trees, revealing a pair of glowing eyes.')
        print('Do you want to KEEP MOVING forward, or do you want to THROW something at the eyes to see what it is?')
        choice3 = input().lower()

        if choice3 == 'keep moving':
            print('You continue down the path, eventually finding your way out of the forest. You have successfully navigated the forest!')
        elif choice3 == 'throw':
            print('You throw a nearby rock at the eyes in the trees. The rock hits a small creature, which scurries away. You continue down the path, eventually finding your way out of the forest.')
        else:
            print('Invalid choice. Please try again.')

    elif choice2 == 'look':
        print('You shine your light into the trees, revealing a pair of glowing eyes. A small creature leaps out and lands at your feet.')
        print("It's a friendly forest sprite, grateful for your light as it was lost in the dark. It offers to GUIDE you out of the forest.")
        print('Do you want to ACCEPT its help, or continue on your own?')
        choice3 = input().lower()

        if choice3 == 'accept':
            print('The forest sprite leads you safely out of the forest. You have successfully navigated the forest!')
        elif choice3 == 'continue' or choice3 == 'continue on your own':
            print('You decide to continue on your own, but you soon get lost in the darkness. The forest sprite tries to help, but you are unable to find your way out. Game over.')
        else:
            print('Invalid choice. Please try again.')
    else:
        print('Invalid choice. Please try again.')
else:
    print('Invalid choice. Please try again.')
