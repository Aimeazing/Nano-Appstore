# Game One | Guess the number | Finished

import os                  # Import a library for clearing the terminal
import pyfiglet            # Import a library for ASCII art
from random import randint # Import randint function from the random library

# Assigns text colours
greenText  = '\033[92m'
redText    = '\033[91m'
blueText   = '\033[36m'
purpleText = '\033[35m'
reset      = '\033[0m' # Reset text colour to default

def intInput(vraag):
    userInput = 'a'
    while not userInput.isdigit():
        userInput = input(vraag)
    return int(userInput)


# Generate and print ASCII art
def  asciiArt1(userName):
    ascii_art = pyfiglet.figlet_format("Guess The Number")
    print(purpleText, ascii_art, reset)
    print("Welcome to 'Guess the number'!")
    startGame1(userName)


# Menu
def startGame1(userName):
    players = input(f"Would you like : (Numbers only!)\n{blueText}| multiplayer [1] | singleplayer [2] |\n{reset}  ").lower()

    if   players == '1' or players == 'multiplayer':
        multiPlayer(userName)
    elif players == '2' or players == 'singleplayer':
        singlePlayer(userName)
    else:
        print(f"{redText}Invalid option!{reset}")
        startGame1(userName) # Ask again


# Set up for the singleplayer option
def singlePlayer(userName):
    guessCount = 1
    maxGuesses = 10

    difficulty = input(f"What difficulty do you want?\n{blueText}| easy | medium | hard | impossible |\n{reset}").lower()
            
    if   difficulty == 'easy':
        number = randint(0, 49)
        difficultyRange = 49
        print(f"Alright {userName}, I picked a number between 0 and 50.\n You have 10 guesses.")
    elif difficulty == 'medium':
        number = randint(0, 99)
        difficultyRange = 99
        print(f"Alright {userName}, I picked a number between 0 and 100.\n You have 10 guesses.")
    elif difficulty == 'hard':
        number = randint(0, 499)
        difficultyRange = 499
        print(f"Alright {userName}, I picked a number between 0 and 500.\n You have 10 guesses.")
    elif difficulty == 'impossible':
        number = randint(0, 999)
        difficultyRange = 999
        print(f"Alright , I picked a number between 0 and 1000.\n You have 10 guesses.")
    else:
        print(f"{redText}Invalid difficulty!{reset}")
        singlePlayer(userName) # Ask again
    
    # Start the game and bring variables along
    playGame(guessCount, maxGuesses, number, difficultyRange, userName)


# Set up for the multiplayer option
def multiPlayer(userName):
    guessCount = 1
    userName2  = input("What username does player 2 want to play with: ")
    number     = intInput(f"{userName}, please pick a number:  ")
    maxGuesses = intInput(f"How many guesses does {userName2} get:  ")

    os.system('cls')  # Clear the terminal (Only for Windows)
    #os.system('clear') #Clear the terminal (Linux and macOS)
    print(f"{userName2}, you have {maxGuesses} guesses.")

    # Start the game and bring variables along
    playGame(guessCount, maxGuesses, number, None, userName2)


# All the game logic
def playGame(guessCount, maxGuesses, number, difficultyRange, userName):
    # Loop for the maximum guesses allowed
    for guessCount in range(1, maxGuesses+1):
        guess = int(input(f"{userName} please make your guess, you have {(maxGuesses - guessCount) + 1} guesses left:  "))

        # When there is a difficulty range, keep the user within the range
        if difficultyRange is not None:
            if   guess < 0:
                print(f"Your input is out of range, guess between: 0 and {int(difficultyRange)+1}, you guessed to low")
                continue
            elif guess > difficultyRange:
                print(f"Your input is out of range, guess between: 0 and {int(difficultyRange)+1}, you guessed to high")
                continue

        # Give feedback on the guess
        if   guess > number and guessCount >= 1:
            print("Lower!")
        elif guess < number and guessCount >= 1:
            print("higher!")
        elif guess == number:
            print(f"{greenText}You have guessed correctly in {guessCount} guesses, congrats :)!{reset}")
            break # Exit the loop if the guess is correct
    else:
        print(f"unfortunately you are all out of guesses :(. The correct  number was {number}")