'''
pick a word
Tell the player:
  1. Length of word
  2. Number of guesses
User guesses
  store letter guessed in list
if true -> display
if false -> -1 guess
continue until:
  1. Out of guesses
  2. Got the word
    ALL letter in word are in guessed list
'''
import random
import string

def getWordList():
  inFile = open("HIDDEN_WORDS.txt", "r")
  line = inFile.readline()
  wordList = line.split()
  print (" ", len(wordList), "words read!")
  return wordList

def pickWord(wordList):
  return random.choice(wordList)

def isWin(hiddenWord, lettersGuessed):
  for letter in hiddenWord:
    if letter not in lettersGuessed:
      return False
  return True

def displayWord(hiddenWord, lettersGuessed):
  result = ""
  for letter in hiddenWord:
    if letter in lettersGuessed:
      result += letter + " "
    else:
      result += "_ "
  return result[:-1]

def gameHangMan(hiddenWord):
  print ("Welcome to Hangman !!!")
  print ("The secret word has " + str(len(hiddenWord)) + " letters")
  letterGuessed = []
  numOfTurnsLeft = 10

  print (displayWord(hiddenWord,letterGuessed))
  win = isWin(hiddenWord,letterGuessed)
  while (numOfTurnsLeft > 0 and not win ):
    letter = input("Enter your guess: ").lower()
    if letter not in letterGuessed:
      letterGuessed.append(letter)
    else:
      print ("You have already guessed this, try again!")
      continue

    if letter in hiddenWord:
      print ("Yay, you got it!")
    else:
      print ("Sorry, the word does not contain letter " + letter)
      numOfTurnsLeft -= 1
    print (displayWord(hiddenWord,letterGuessed))
    print("Your have "+ str(numOfTurnsLeft) + " turns left")
    displayWord(hiddenWord,letterGuessed)
    win = isWin(hiddenWord,letterGuessed)

  if(win):
    print ("Congratulations! You won!")
  else:
    print ("Sorry! You are out of turns.")
    print ("The hidden word is " + hiddenWord)


wordList = getWordList()
hiddenWord = pickWord(wordList).lower()
gameHangMan(hiddenWord)
