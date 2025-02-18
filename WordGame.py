#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    spot = word.find(letter)
    if spot >= 0:
        return True
    else:
       return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    if word[spot] == letter:
     return True
    else:

     return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    result = ""
    for spot in range(5) :
       letter = myGuess[spot]
    if inSpot(letter, word, spot):
       result = result + letter. upper()
    elif inWord(letter, word):
       result = result + letter.lower()
    else:
       result = result + "*"

    return result

       

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess
    guessNumber = 0
    guess = ""
    while guessNumber < 6 and guess != todayWord:

    #Ask user for their guess
    guess = input("Enter your guess")
    guessNumber = guessNumber + 1

    #Give feedback using on their word:
    feedback = rateGuess(guess, todayWord)
    print(feedback)

    print("The word was", todayWord)
    if guess == todayWord:
       print("You Win")





if __name__ == '__main__':
  main()
