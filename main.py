global wordList
global wordLength
global numGuesses
global debugEnabled
global guessedLetters
global wordProgress


# Load words into wordList from file
def readFile(filename):
    try:
        with open(filename) as f:
            # Load global variable into this scope
            global wordList
            global wordLength

            # Load each word from dictionary.txt into wordList if matches length specified
            while True:
                word = f.readline().rstrip()
                if(len(word)==wordLength):
                    wordList.append(word)
                if not word:
                    break

    except IOError:
        print("Error: File does not exist")
        exit(-1)


# Prompt user for word length with valid input check
def promptWordLength():
    while True:
        wordLength = input("What is the word length? ")
        if (wordLength.isdigit()):
            if (int(wordLength) > 0 and int(wordLength) < 137):
                return int(wordLength)
            else:
                print("Invalid length")
        else:
            print("Invalid number")


# Prompt user for number of guesses with valid input check
def promptNumGuesses():
    while True:
        numGuesses = input("What is the number of guesses? ")
        if (numGuesses.isdigit()):
            if (int(numGuesses) > 0):
                return int(numGuesses)
            else:
                print("Invalid number")
        else:
            print("Invalid number")


# Prompt user for displaying running total of remaining words in list with valid input check
def promptDebug():
    while True:
        numGuesses = input("Turn on debug mode?(0/1) ")
        if (numGuesses.isdigit()):
            if (int(numGuesses) == 1):
                return True
            elif (int(numGuesses) == 0):
                return False
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")


# Print number of guesses , guessed letters, word progress, and debug information if enabled
def printStats():
    global numGuesses
    global guessedLetters
    global wordProgress
    global debugEnabled
    global wordList

    print()
    print("Guesses remaining: " + str(numGuesses))
    if (len(guessedLetters) != 0):
        print("Guessed letters: ", end="")
        print(",".join(list(guessedLetters)))
    else:
        print("Guessed letters: ")
    print("Word progress: " + wordProgress)

    if (debugEnabled):
        print("Number of Remaining possible words: " + str(len(wordList)))
        print("Remaining possible words: ", end="")
        print(wordList)


# Prompts user for a letter and returns it with valid input check and check if already guessed
def promptLetter():
    global guessedLetters
    while True:
        letter = input("Guess a letter: ")
        if (letter.isalpha()):
            if (len(letter) == 1):
                if (letter not in guessedLetters):
                    addLetter(letter)
                    return letter
                else:
                    print("Letter already guessed")
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")


# Adds letter to list of guessed letters
def addLetter(letter):
    global guessedLetters
    guessedLetters.add(letter)
    #if (debugEnabled):
    #    print("Added " + letter + " to guessed")
    #    print(guessedLetters)


# Determine which word family has the most words to pick from, update word progress and available pool of words
def groupFamilies(guessedLetter):
    global wordList
    global debugEnabled
    global wordProgress

    wordDictionary = {"debugKey": []}
    for word in wordList:
        # Key value for dictionary
        wordPattern = ""

        # For each letter in the word generate the word pattern matching the letter
        for letter in word:
            if (letter == guessedLetter):
                wordPattern += letter
            else:
                wordPattern += "-"
        #if (debugEnabled):
        #    print("Word pattern for " + word + " is " + wordPattern)

        # Does this key exist in dictionary yet? If so append word to the list stored at key
        if (wordPattern in wordDictionary):
            wordDictionary[wordPattern].append(word)
        else:  # Otherwise create new key and new array as value of key
            wordDictionary[wordPattern] = [word]

    #if (debugEnabled):
    #    print("Updated wordDictionary")
    #    print(wordDictionary)

    # For each key in the updated word dictionary, check the len of each list stored at each key, find max
    maxLen = 0
    maxKey = ""
    for key in wordDictionary:
        currentLen = len(wordDictionary[key])
        if (currentLen > maxLen):
            maxLen = currentLen
            maxKey = key
    if (debugEnabled):
        print("Family with max values is: " + str(maxKey))

    # Update wordList to match max family
    wordList = wordDictionary[maxKey]
    #if (debugEnabled):
    #    print("Wordlist updated")
    #    print(wordList)

    # Update word progress to match new key
    newProgress = wordProgress
    # For each letter in old word progress, compare with the max key found
    for i in range(0, len(wordProgress)):
        # If there is an empty space that is not empty in max key, replace it with letter
        if (wordProgress[i] == "-" and maxKey[i] != "-"):
            newProgress = newProgress[:i] + maxKey[i] + newProgress[i + 1:]
    wordProgress = newProgress
    #if (debugEnabled):
    #    print("wordProgress updated")
    #    print(wordProgress)


# Play a game of hangman
def playHangman():
    # Load the wordlist into local space
    global wordList
    global wordLength
    global numGuesses
    global debugEnabled
    global guessedLetters
    global wordProgress

    # Prompt for word length, number of guesses, and debug mode
    wordLength = promptWordLength()
    numGuesses = promptNumGuesses()
    debugEnabled = promptDebug()

    # Initialize wordList to empty list
    wordList = []

    # Load initial dictionary of words with specified length to wordList
    readFile("dictionary.txt")

    # Initialize wordProgress to blacked out at the start of the game
    wordProgress = ""
    for i in range(0, wordLength):
        wordProgress += "-"

    # Initialize guessedLetters to empty set
    guessedLetters = set()

    while (numGuesses > 0):
        # Print status of game
        printStats()

        if(len(wordList)==0):
            print("No words found with length " + str(wordLength))
            break

        # Prompt player for a letter and update list of guessed letters
        guessedLetter = promptLetter()

        # Group words into families
        groupFamilies(guessedLetter)

        # Check win condition
        if (wordProgress == wordList[0]):
            print()
            print("You won!")
            print("The word was " + wordList[0])
            print()
            break

        numGuesses -= 1

    if (numGuesses == 0):
        print()
        print("You lost!")
        print("The word was " + wordList[0])
        print()


while True:
    print()
    print("Welcome to Evil Hangman")
    print("Created by Justin Mercado")
    print("March 21, 2021")
    print()

    playHangman()
    playAgain = input("Play again?(0/1) ")
    if (playAgain.isdigit()):
        if (int(playAgain) == 0):
            exit(0)
    else:
        exit(0)
