# MIT License
# Copyright (c) 2022 Mahmoud Harmouch

if __name__ == "__main__":
	print( '''
	    /_/_/_/
	  .'     '.  
	 /  o   o  \   
	(|    <    |)   
	 \  '---'  /   
	  '._____.'  
	''')
	print("Welcome to 'Guess Your Number Game'!")
	player_name = input('What is your name?\n')
	print("Hello " + player_name + " !")
	min_ = 1
	max_ = 50
	print(f"Think of a number between {min_} and {max_}.")
	print("I am trying to guess it in as few attempts as possible.\n")
	max_tries = 20;
	offset = round((max_ + min_)/2)
	guess = offset
	for tries in range(max_tries):
		answer = input(f"Is your number lower than {guess}?(yes/no)\n")
		if answer == 'yes':
			guess -= round(offset/2)
		else :
			guess += round(offset/2)
		offset = round(offset/2)
		answer = input(f"Is your number equal to {guess}?(yes/no)\n")
		if answer == 'yes':
			print( '''
	    /_/_/_/
	  .'     '.  
	 /  x   x  \   
	(|    <    |)   
	 \  '---'  /   
	  '._____.'  
	''')
			print("Wohooo! I guessed it! your number was", guess)
			print("And it only took me", tries, "tries!\n")
			print("Nice!\n")
			break
		else:
			print( '''
	    /_/_/_/
	  .'     '.  
	 /  o   o  \   
	(|    <    |)   
	 \  .---.  /   
	  '._____.'  
	''')
			print("Alright! Let's try again")
		if tries == max_tries - 1:
			print("I have reached the maximum number of attempts!")
			input("\n\nTell me what was your number?")
			print("Alright, cool! I will try to guess it next time...")
			break
		print(f"I only have { max_tries - tries - 1} {'tries' if tries < max_tries - 2 else 'try'} left!\n")
	


