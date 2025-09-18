# Game Four | Rock paper scissors | Finished

import os                  # Import a library for clearing the terminal
import pyfiglet            # Import a library for ASCII art
from random import shuffle # Import shuffle function from the random library

# Assigns text colours
greenText  = '\033[92m'
redText    = '\033[91m'
blueText   = '\033[36m'
purpleText = '\033[35m'
reset      = '\033[0m' # Reset text colour to default

# Generate and print ASCII art
def asciiArt4(userName):
    ascii_art = pyfiglet.figlet_format("Rock paper scissors")
    print(purpleText, ascii_art, reset)
    print("Welcome to 'Rock paper scissors'!")
    startGame4(userName)


# Menu
def startGame4(userName):
    players = input(f"Would you like :\n{blueText}| multiplayer [1] | singleplayer [2] |\n{reset}  ").lower()

    if   players == '1' or players == 'multiplayer':
        multiPlayer(userName)
    elif players == '2' or players == 'singleplayer':
        singlePlayer(userName)
    else:
        print(f"{redText}Invalid option!{reset}")
        startGame4(userName) # Ask again


# Set up for the singleplayer option
def singlePlayer(userName):
    optionsList = ['1', '2', '3']
    shuffle(optionsList)

    userName2 = 'Computer'
    option1   = optionsList[0]
    option2   = input(f"{userName}, What do you choose: \n{blueText}| Rock [1] | Paper [2] | scissors [3] |\n{reset}").lower()
    if option2 not in ['1', 'rock', '2', 'paper', '3', 'scissors']:
        print(f"{redText}Invalid option!{reset}")
        singlePlayer(userName)
    # Start the game and bring variables along
    playGame(option1, option2, userName, userName2)


# Set up for the multiplayer option
def multiPlayer(userName):
    option1 = 0
    while option1 not in ['1', 'rock', '2', 'paper', '3', 'scissors']:
        option1 = input(f"{userName}, What do you choose: \n{blueText}| Rock [1] | Paper [2] | scissors [3] |\n{reset}").lower()

    os.system('cls')  # Clear the terminal (Only for Windows)
    #os.system('clear') #Clear the terminal (Linux and macOS)

    userName2 = input("What username does player 2 want to play with: ").lower()
    option2 = 0
    while option2 not in ['1', 'rock', '2', 'paper', '3', 'scissors']:
        option2 = input(f"{userName2}, What do you choose: \n{blueText}| Rock [1] | Paper [2] | scissors [3] |\n{reset}").lower()

    # Start the game and bring variables along
    playGame(option1, option2, userName, userName2)


# All the game logic
def playGame(option1, option2, userName, userName2):
    if   option1 == option2:
        print("It is a tie!")
    elif (option1 == '1' or option1 == 'rock')     and (option2 == '2' or option2 == 'paper'):
        print(f"{greenText}{userName2} wins! (Paper beats Rock){reset}")
    elif (option1 == '1' or option1 == 'rock')     and (option2 == '3' or option2 == 'scissors'):
        print(f"{greenText}{userName} wins! (Rock beats Scissors){reset}")
    elif (option1 == '2' or option1 == 'paper')    and (option2 == '1' or option2 == 'rock'):
        print(f"{greenText}{userName} wins! (Paper beats Rock){reset}")
    elif (option1 == '2' or option1 == 'paper')    and (option2 == '3' or option2 == 'scissors'):
        print(f"{greenText}{userName2} wins! (Scissors beats Paper){reset}")
    elif (option1 == '3' or option1 == 'scissors') and (option2 == '1' or option2 == 'rock'):
        print(f"{greenText}{userName2} wins! (Rock beats Scissors){reset}")
    elif (option1 == '3' or option1 == 'scissors') and (option2 == '2' or option2 == 'paper'):
        print(f"{greenText}{userName} wins! (Scissors beats Paper){reset}")



























































