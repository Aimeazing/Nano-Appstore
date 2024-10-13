# Game Three | Riddles | Finished

import pyfiglet            # Import a library for ASCII art
from random import shuffle # Import shuffle function from the random library

# Assigns text colours
greenText  = '\033[92m'
redText    = '\033[91m'
blueText   = '\033[36m'
purpleText = '\033[35m'
reset      = '\033[0m' # Reset text colour to default


# Generate and print ASCII art
def  asciiArt3(userName):
    ascii_art = pyfiglet.figlet_format("Riddles")
    print(purpleText, ascii_art, reset)
    print("Welcome to 'Riddles'!")
    startGame3(userName)


# variables for category animals
animalEasy1   = "What do you call a bear with no teeth?;A gummy bear"
animalEasy2   = "What creature is smarter than a talking parrot?;A spelling bee"
animalEasy3   = "What do you call a snail on a ship?;A snailor"

animalMedium1 = "What is orange and sounds like a parrot?;A carrot."
animalMedium2 = "A farmer has twenty sheep, ten pigs, and ten cows. If we call the pigs cows, how many cows will he have?;Ten cows. We can call the pigs cows, but it doesn't make them cows"

animalHard1   = "I give milk and I have a horn, but I'm not a cow. What am I?;A milk truck"
animalHard2   = "Why did the fly never land on the computer?;He was afraid of the world wide web"
animalHard3   = "How does a bee get to school?;On a buzz"

# variables for category Objects
objectEasy1   = "What has many holes but still holds water?;A sponge!"
objectEasy2   = "I'm tall when I'm young, and I'm short when I'm old. What am I?;A candle!"

objectMedium1 = "What has a neck but no head?;A bottle!"
objectMedium2 = "What has keys but can't open locks?;A piano"
objectMedium3 = "What gets wetter as it dries?;A towel"

objectHard1   = "I have hundreds of wheels, but move I do not. Call me what I am: call me a lot. What am I?;A parking lot"
objectHard2   = "What has a face and two hands but no arms or legs?;A clock"
objectHard3   = "What can travel around the world while staying in a corner?;A stamp"

# variables for category Random
randomEasy1   = "What do you call a fake noodle?;An impasta!"
randomEasy2   = "What does a house wear?;Ad-dress"
randomEasy3   = "What is always in front of you but can't be seen?;The future"

randomMedium1 = "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?;An echo!"
randomMedium2 = "What can you catch but not throw?;A cold!"

randomHard1   = "Why are As like flowers?;Because Bs come after them"
randomHard2   = "What has to be broken before you can use it?;An egg!"
randomHard3   = " During what month do people sleep the least?;February. It's the shortest month!"


# Categorizing the chosen riddles in lists
def startGame3(userName):
    catagorie = int(input(f"{userName} What catagory would you like? (Numbers only!)\n{blueText}| Animals [1] | Objects [2] | Random [3] |{reset} "))
    if   catagorie == 1: # Catagory Animals
        difficulty  = int(input(f"What dificulty do you want to play on? (Numbers only!)\n{blueText}| Easy [1] | Medium [2] | Hard [3] |{reset} "))
        if   difficulty == 1:
            riddles = [animalEasy1, animalEasy2, animalEasy3] # Easy riddles
            playGame(riddles)
        elif difficulty == 2:
            riddles = [animalMedium1, animalMedium2]          # Medium riddles
            playGame(riddles)
        elif difficulty == 3:
            riddles = [animalHard1, animalHard2, animalHard3] # Hard riddles
            playGame(riddles)
        else:
            print(f"{redText}Difficulty level not found{reset}")
            startGame3(userName) # Ask again
    elif catagorie == 2: # Catagory Objects
        difficulty  = int(input(f"What dificulty do you want to play on? (Numbers only!)\n{blueText}| Easy [1] | Medium [2] | Hard [3] |{reset} "))
        if   difficulty == 1:
            riddles = [objectEasy1, objectEasy2]                    # Easy riddles
            playGame(riddles)
        elif difficulty == 2:
            riddles = [objectMedium1, objectMedium2, objectMedium3] # Medium riddles
            playGame(riddles)
        elif difficulty == 3:
            riddles = [objectHard1, objectHard2, objectHard3]       # Hard riddles
            playGame(riddles)
        else:
            print(f"{redText}Difficulty level not found{reset}")
            startGame3(userName) # Ask again
    elif catagorie == 3: # Catagory Random
        difficulty  = int(input(f"What dificulty do you want to play on? (Numbers only!)\n{blueText}| Easy [1] | Medium [2] | Hard [3] |{reset} "))
        if   difficulty == 1:
            riddles = [randomEasy1, randomEasy2, randomEasy3] # Easy riddles
            playGame(riddles)
        elif difficulty == 2:
            riddles = [randomMedium1, randomMedium2]          # Medium riddles
            playGame(riddles)
        elif difficulty == 3:
            riddles = [randomHard1, randomHard2, randomHard3] # Hard riddles
            playGame(riddles)
        else:
            print(f"{redText}Difficulty level not found{reset}")
            startGame3(userName) # Ask again
    else:
        print(f"{redText}Catagory not found{reset}")
        startGame3(userName) # Ask again


# All the game logic
def playGame(riddles):
    # Randomize the order of the riddle list
    shuffle(riddles)

    # Select a random riddle from the list
    for left in range(len(riddles)):
        question, answer = riddles[left].split(';') # Split riddle and answer

        # Wait for the users cue to give the answer
        helpAnswer = input(f"Riddle: {question}\n Type 'a' for the answer! ").lower()
        if helpAnswer == 'a':
            print(f"Answer: {answer}")

        # Only ask if there are more riddles left
        if left < len(riddles) - 1: # Stay in the loop when it is not the last riddle
            continueRiddles = input("Do you want another riddle? ").lower()
            if continueRiddles == 'no':
                break # Exit the loop
        
    

            















