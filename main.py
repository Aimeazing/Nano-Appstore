# AppStore | Apptitude | Ongoing

import os                      # Import a library for clearing the terminal
import pyfiglet                # Import a library for ASCII art
from datetime import datetime  # Import datetime function from the datetime library
from Game01   import asciiArt1 # Import function from Game 1
from Game02   import asciiArt2 # Import function from Game 2
from Game03   import asciiArt3 # Import function from Game 3
from Game04   import asciiArt4 # Import function from Game 4

# Assigns text colours
greenText  = '\033[92m'
redText    = '\033[91m'
blueText   = '\033[36m'
purpleText = '\033[35m'
reset      = '\033[0m' # Reset text colour to default

# Generate and print ASCII art
ascii_art = pyfiglet.figlet_format("Apptitude")
print(purpleText, ascii_art, reset)

# User has to log in with a username and password
def login():
    userName = input(f"{blueText}Please type your username: {reset}")

    # Checking the current time
    currentTime = datetime.now() 
    hour        = currentTime.hour
    if    6 <= hour <12:
        print(f"Good morning {userName}!")
    elif 12 <= hour <18:
        print(f"Good afternoon {userName}!")
    else:
        print(f"Good evening {userName}!")

    # Password
    password = 'FreePass123' 
    passwordGuess = input(f"{blueText}Please enter your password: {reset}")

    while passwordGuess != password:
        print(f"{redText}Password does not match, please try again{reset}")
        passwordGuess = input(f"{blueText}Please enter your password: {reset}")

    menu(userName)

def menu(userName):
    while True: # Looping until user chooses to exit
        os.system('cls')  # Clear the terminal (Only for Windows)
        #os.system('clear') #Clear the terminal (Linux and macOS)
        game = int(input(f"What game would you like to play? (Numbers only!)\n{blueText}| Guess the number [1] | Hangman [2] | Riddles [3] | Rock paper scissors [4] | Exit [0] |{reset} "))

        if   game == 1:
            asciiArt1(userName)
        elif game == 2:
            asciiArt2(userName)
        elif game == 3:
            asciiArt3(userName)
        elif game == 4:
            asciiArt4(userName)
        elif game == 0:
            print(f"Thank you for playing, {userName}!")
            break # Exit the loop
        else:
            print(f"{redText}Invalid choice.{reset}")
            menu(userName)

        again = input(f"{blueText}Do you want to go back to the menu?{reset}").lower()
        if again == 'no': 
            print("Goodbye, have a nice day!")
            break # Exit the loop

login()

