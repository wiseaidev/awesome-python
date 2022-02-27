# MIT License
# Copyright (c) 2022 Mahmoud Harmouch

import random
import sys

if __name__ == "__main__":
	print( '''
	    /_/_/_/
	  .'     '.  
	 /  o   o  \   
	(|    <    |)   
	 \  '---'  /   
	  '._____.'  
	''')
	print("Welcome to 'Guess My Number Game'!")
	player_name = input('What is your name?\n')
	print("Hello " + player_name + " !")
	min_ = 1
	max_ = 50
	print(f"I'm thinking of a number between {min_} and {max_}.")
	print("Try to guess it in as few attempts as possible.\n")
	gen_number = random.randint(min_, max_)
	guess = None
	max_tries = 20;
	for tries in range(max_tries):	
		try:
			input_ = input(f"Take a guess between {min_} and {max_} ('q' to exit)\n")
			if input_ == 'q':
				sys.exit("Goodbye " + player_name + "!" + " See you later!")
			else :
				guess = int(input_)
		except ValueError:
			sys.exit("Not a valid guess! Exiting!")
		if guess > gen_number:
			print( '''
	    /_/_/_/
	  .'     '.  
	 /  o   o  \   
	(|    <    |)   
	 \  .---.  /   
	  '._____.'  
	''')
			print("Try to guess a lower number...")
		elif guess < gen_number:
			print( '''
	    /_/_/_/
	  .'     '.  
	 /  o   o  \   
	(|    <    |)   
	 \  .---.  /   
	  '._____.'  
	''')
			print("Try to guess a higher number...")
		else:
			print( '''
	    /_/_/_/
	  .'     '.  
	 /  x   x  \   
	(|    <    |)   
	 \  '---'  /   
	  '._____.'  
	''')
			print("Congrats! You guessed it! The number was", gen_number)
			print("And it only took you", tries, "tries!\n")
			print("Nice!\n")
			break
		if tries == max_tries - 1:
			print("You have reached the maximum number of attempts! Hard Luck!")
			print("The magic number was", gen_number)
			break
		print(f"{ max_tries - tries - 1} {'tries' if tries < max_tries - 2 else 'try'} left!\n")
	
	input("\n\nPress the <return> key to exit...")


