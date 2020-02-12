"""finalproject.py: A simple game of hangman."""

__author__ = "Kyle Van Blaricom"
__email__ = "vanblakp@mail.uc.edu"

import random

words = open('words.txt', encoding='ascii').read().upper().split()

def getWord():
    word = words[random.randint(0,len(words))]
    return word

def playerGuess(incorrectGuess, correctGuess):
    Guess = False
    while True:
        print("Enter your guess:")
        guess = input()
        guess = guess.upper()
        if guessedLetters(guess, incorrectGuess, correctGuess) is False:
                print(""), print("You already guessed that letter!")
        elif len(guess) != 1:
            print(""), print("You may only enter a single letter.")
        elif guess.isalpha() is False:
            print(""), print("You must enter a letter.")
        else:
            return guess

def guessedLetters(guess, incorrectGuess, correctGuess):
    i = 0
    if len(incorrectGuess) == 0:
        if len(correctGuess) == 0:
            return True
    while i < len(correctGuess):
        if correctGuess[i] == guess:
                return False
        i = i + 1
    i = 0
    while i < len(incorrectGuess):
        if incorrectGuess[i] == guess:
            return False
        i = i + 1
    return True

def wordCheck(word, letter):
    if letter in word:
        return True
    return False

def playerPoints(wordCheck, letter, points, correctGuess, incorrectGuess):
    print("")
    if wordCheck is False:
        points = points - 1
        print(HANGMAN_PICS[len(incorrectGuess) + 1]), print("")
        print("Sorry, the word does not contain that letter.")
        incorrectGuess.append(letter)
        return points, incorrectGuess, correctGuess
    else:
        print(HANGMAN_PICS[len(incorrectGuess)]), print("")
        print("Well done! The word contains that letter.")
        correctGuess.append(letter)
        return points, incorrectGuess, correctGuess

def printInfo(word, correctGuess, incorrectGuess):
    i = 0
    j = 0
    counter = 0
    print("")
    print("YOUR WORD: ")
    while i < len(word):
        if len(correctGuess) == 0:
            print(" _ ", end = "")
            counter = counter + 1
        while j < len(correctGuess):
            if word[i] == correctGuess[j]:
                print(word[i], "", end = "")
                break
            elif j == len(correctGuess) - 1:
                print(" _ ", end = "")
                counter = counter + 1
            j = j + 1
        j = 0
        i = i + 1
    print(""), print("")
    i = 0
    print("INCORRECT LETTERS USED: ")
    while i < len(incorrectGuess):
        print(incorrectGuess[i], ", ", end = "")
        i = i + 1
    print(""), print("")
    if counter == 0:
        "Congratulations! You have won the Hang Man!"
        return True
    return False

def playAgain():
    print(""), print("Would you like to play the Hang Man again?")
    answer = input()
    answer = answer.upper()
    while answer != "YES" and answer != "NO":
        print("You must enter yes or no.")
        answer = input()
        answer = answer.upper()
    if answer == "YES":
        return True
    elif answer == "NO":
        return False

def playGame():
    wins = 0
    losses = 0
    Answer = True
    while Answer is True:
        word = getWord()
        points = 6
        correctGuess = []
        incorrectGuess = []
        print(HANGMAN_PICS[len(incorrectGuess)]), print("")
        printInfo(word, correctGuess, incorrectGuess)
        while points > 0:
            letter = playerGuess(incorrectGuess, correctGuess)
            points, incorrectGuess, correctGuess = playerPoints(wordCheck(word, letter), letter, points, correctGuess, incorrectGuess)
            if points == 0:
                losses = losses + 1
                print("You lost! The word was ", word, ". Better luck next time...")
                print("You have won ", wins, " times and lost ", losses, " times.")
                Answer = playAgain()
            elif printInfo(word, correctGuess, incorrectGuess) is True:
                points = 0
                wins = wins + 1
                print("Congratulations. You have saved the Hang Man!")
                print("You have won ", wins, " times and lost ", losses, " times!")
                Answer = playAgain()

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  o   |
      |
      |
     ===''', '''
  +---+
  o   |
  |   |
      |
     ===''', '''
  +---+
  o   |
 /|   |
      |
     ===''', '''
  +---+
  o   |
 /|\  |
      |
     ===''', '''
  +---+
  o   |
 /|\  |
 /    |
     ===''', '''
  +---+
  o   |
 /|\  |
 / \  |
     ===''']

playGame()
