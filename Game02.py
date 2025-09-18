# Game Two | Hangman | Finished

import os                 # Import a library for clearing the terminal
import pyfiglet           # Import a library for ASCII art
from random import choice # Import choice function from the random library

# Assigns text colours
greenText  = '\033[92m'
redText    = '\033[91m'
blueText   = '\033[36m'
purpleText = '\033[35m'
reset      = '\033[0m' # Reset text colour to default


# Generate and print ASCII art
def asciiArt2(userName):
    ascii_art = pyfiglet.figlet_format("Hangman")
    print(purpleText, ascii_art, reset)
    print("Welcome to 'Hangman'!")
    startGame2(userName)


# Menu
def startGame2(userName): 
    players = 0
    while players not in ['1', '2', 'singleplayer', 'multiplayer']:
        players = input(f"Would you like :\n{blueText}| singleplayer [1] | multiplayer [2] |\n{reset}  ").lower()

    if   players == '2' or players == 'multiPlayer':
        multiPlayer(userName)
    elif players == '1' or players == 'singleplayer':
        singlePlayer(userName)


# Set up for the singleplayer option
def singlePlayer(userName):
    with open('C:/Users/aimbl/Desktop/Git-project/mostCommonWords.txt') as openFile:
        words = openFile.readlines()

    words      = [word.strip() for word in words]
    word       = choice(words)
    maxGuesses = 7
    print(f"{userName}, your word contains {len(word)} letters. You have {maxGuesses} guesses!")

    # Start the game and bring variables along
    playGame(word, 0, maxGuesses)


# Set up for the multiplayer option
def multiPlayer(userName):
    word              = input(f"{userName}, please pick a word:  ").lower()
    userName2         = input("What username does player 2 want to play with: ") 
    lengthWord        = len(word) 
    maxGuesses        = 7

    os.system('cls')  # Clear the terminal (Only for Windows)
    #os.system('clear') #Clear the terminal (Linux and macOS)
    print(f"{userName2}, you have {maxGuesses} guesses and your word has {lengthWord} characters")

    # Start the game and bring variables along
    playGame(word, 0, maxGuesses)

# List of hangman in ASCII art based on the amount of mistakes
hangMan = [
    """
       ------
            |
            |
            |
            |
            |
    =========
    """,  # 0 mistakes
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,  # 1 mistakes
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,  # 2 mistake
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,  # 3 mistakes
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,  # 4 mistakes
    """
       ------
       |    |
       O    |
      /|\\   |
             |
            |
    =========
    """,  # 5 mistakes
    """
       ------
       |    |
       O    |
      /|\\   |
      /      |
            |
    =========
    """,  # 6 mistakes
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """  # 7 mistakes
]


# All the game logic
def playGame(word, guessCount, maxGuesses):
    wrongLetters   = ""
    guessedLetters = []    
    wordLetters    = list(word)
    notGuessedYet  = ["_"]*len(word) # Create list of underscores based the word length

    print(notGuessedYet) # Display the beginning state of the word

    # Loop until the user is out of guesses and the word is not guesses yet
    while (guessCount < maxGuesses) and ("_" in notGuessedYet):
        guess = 0
        while guess not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            guess = input(f"Make your guess, {maxGuesses - guessCount} guesses left:  ").lower()
        
        if  guess in guessedLetters:
            print("You have already guessed this letter!")
            continue
        elif guess in wordLetters:
            print(f"{greenText}Correct!{reset}")
            guessedLetters.append(guess)
            position = 0 #Current position in the list
            # Checks the guess for each letter in the list if so, it will be replaced
            for letter in wordLetters: 
                if letter == guess:
                    notGuessedYet[position] = guess
                position = position + 1
        else:
            if guess in wrongLetters:
                print(f"{redText}You have already tried this letter and it does not appear in the word! try again.{reset}")
                guessCount = guessCount + 1
            else:
                print(f"{redText}This letter does not appear in your word, try again.{reset}")
                wrongLetters = wrongLetters + guess
                guessCount = guessCount + 1

            print(hangMan[guessCount])

        # Display the current state of the word
        print(notGuessedYet)
        print(f"Wrong letters: {wrongLetters}") # Display al wrong guessed letters

    # checking if there are still unguessed letters in the word
    if  "_" not in notGuessedYet:
        print(f"{greenText}Congratulations! you have guessed the word correct!{reset}")
    else:
        print(f"{redText}Unfortunately you are out of guesses :/. The word was: {word}{reset}")