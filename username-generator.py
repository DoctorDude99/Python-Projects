# Programmer: Ibrahim
# Description: Simple password generator in Python

import random
import sys

choice = 0

while choice != 1 or choice !=2:

        print("\nWelcome to Python Password Generator!")
        choice = int(input(print("Press 1 to generate a password\nPress 2 to quit")))
#choice is taken from user

#word 1 is selected
        word1 = random.randint(1,10) 

#word 2 is selected
        word2 = random.randint(1,10)
    
    #first word module
        if word1 == 1:
                word1 = "Slayer"

        elif word1 == 2:
                word1 = "Phantom"

        elif word1 == 3:
                word1 = "Incognito"

        elif word1 == 4:
                word1 = "Mini"

        elif word1 == 5:
                word1 = "Insane"

        elif word1 == 6:
                word1 = "Righteous"

        elif word1 == 7:
                word1 = "Lunar"

        elif word1 == 8:
                word1 = "Spectacular"

        elif word1 == 9:
                word1 = "Specular"

        elif word1 == 10:
                word1 = "Golden"

    #second word module

        if word2 == 1:
                word2 = "Snake"

        elif word2 == 2:
                word2 = "Wizard"

        elif word2 == 3:
                word2 = "Ninja"

        elif word2 == 4:
                word2 = "Glitch"

        elif word2 == 5:
                word2 = "Paradox"

        elif word2 == 6:
                word2 = "Bear"

        elif word2 == 7:
                word2 = "Pirate"

        elif word2 == 8:
                word2 = "Astronaut"

        elif word2 == 9:
                word2 = "Hacker"

        elif word2 == 10:
                word2 = "Phoenix"

        if choice == 1:
                print(word1, word2)
    #activates userName function to make the username

        elif choice == 2:
                sys.exit()
        #exits the program

        #if something other than 1 or 2 is selected
        else:
                print("Sorry, that is not an option..\n")
