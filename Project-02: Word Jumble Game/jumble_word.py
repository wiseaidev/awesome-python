# Word Jumble
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
import random
# words and hints extracted from https://www.k5learning.com/worksheets/vocabulary/5th-grade-jumbled-words-1.pdf
WORDS = ['lightly',
'worth',
'afford',
'forward',
'particular',
'ruin',
'practice',
'clear',
'natural',
'taught']

HINTS = ['With little weight,force or intensity.',
'Having a value of.',
'To be able to manage or bear without serious consequences.',
'Advance, onward',
'Of or relating to a single or specific person, thing or event.',
'A destroyed or decayed building.',
'Repeated performance to acquire proficiency',
'Transparent.',
'Existing in or formed by nature.',
'Imparted knowledge of or skill in.']
if __name__ == "__main__":
	points = 0
	print(
	"""
		Welcome to Word Jumble!
	Unscramble the letters to make a word.
	(Press the enter key at the prompt to quit.)
	"""
	)
	correct = False
	playAgain = True
	while (playAgain==True):
		jumble = ""
		correct = False
		guesses = 0
		# pick one word randomly from the sequence
		index = random.randint(0,len(WORDS)-1) # same as random.randrange(len(WORDS))
		word = WORDS[index]
		correct_ = word
		hint = HINTS[index]
		while len(word) or correct_ == jumble:
			index = random.randrange(len(word))
			jumble += word[index]
			word = word.replace(word[index], '') # remove a char from the string
		print("The jumble is:", jumble)
		tempPoints = 0
		while correct == False:
			guess = input("Enter your guess: ").strip().lower()
			guesses += 1
			if guess == correct_:
				print("That's it! You guessed it in only " + str(guesses) + " tries!\n")
				tempPoints += len(jumble) * 1.25  # some random points
				tempPoints -= round((guesses - 1) / 4.0, 2) # first guess ==> zero
				points += tempPoints
				print(str(tempPoints) + " points this round and a total of " + str(points) + "!\n")
				correct = True
				yesNo = input("Would you like to play again? (yes/no): ")
				if (yesNo == 'yes'):
					playAgain = True
				else:
					playAgain = False
			elif guess == "hint":
				tempPoints -= (1.0 / len(jumble)) * 40
				print("Hint: " + hint)
				correct = False	
				playAgain = True
			elif guess == "quit":
				correct = True	
				playAgain = False
			else:
				sub = round((1.0 / len(jumble)) * 20,2)
				print("Incorrect word, deducting " + str(sub) + " points\n")
				tempPoints -= sub
				playAgain = True
				correct = False
	print("Thanks for playing.")
	input("\n\nPress the enter key to exit.")




