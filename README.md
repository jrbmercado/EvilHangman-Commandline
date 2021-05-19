# Evil Hangman
Hangman but the computer secretly changes the word as you guess to make you lose!

## Installation Instructions
1. Download evilhangman.zip
2. Unzip evilhangman.zip
3. Run evilhangman.exe


## Purpose
1. Practice implementation of Greedy Algorithms
2. Use of dictionaries and sets
3. File handling
4. Data validation and handling


## Tools Used
1. PyCharm
2. SourceTree 
2. Bitbucket


## Logic
1. Initialize a list of words from a dictionary file that matches the length specified at the beginning of the game.
2. For every letter guessed, group all remaining words in the list into word families of the guessed letter.
	- ie. For the letter guessed "e" and the wordset ["echo", "heal", "best", "love"]
		- "echo" word family is e---
		- "heal" word family is -e--
		- "best" word family is -e--
		- "love" word family is ---e
3. Put each unique word family into a dictionary where key=word family and value=array of words of that family.
	- ie. {"e---":["echo"], "-e--":["heal","best"], "---e":["love"]}
4. Find the word family with the most number of words possible.
	- ie. "-e--" because it has 2 possible words while the other word families have only 1
5. Update the remaining list of words to array of words that belong to the max family.
6. Update the word progress to match if a letter has been revealed.
7. Continue game until player runs out of guesses or guesses the word.
8. Ask to play again.
