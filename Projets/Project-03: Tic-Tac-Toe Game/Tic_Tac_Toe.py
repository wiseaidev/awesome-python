# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent
# global constants
# A modified version of the code from: https://www.cs.ucdavis.edu/~gusfield/cs10sp11/tictactoe.py
X = "X"
O = "O"
TIE = "TIE"
NUM_SQUARES = 9
NUMBERS = "012345678"

def display_instruct():
	"""Display game instructions."""
	print(
	"""
Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
This will be a showdown between your human brain and my silicon processor.
You will make your move known by entering a number, 0 - 8. The number
will correspond to the board position as illustrated:
			0 | 1 | 2
			---------
			3 | 4 | 5
			---------
			6 | 7 | 8
Prepare yourself, human. The ultimate battle is about to begin. \n
"""
	)

def ask_number(question, low, high):
	"""Ask for a number within a range."""
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response

def pieces():
	"""Determine if player or computer goes first."""
	go_first = input("Do you require the first move? (y/n): ").strip().lower()
	if go_first == "y":
		print("\nThen take the first move. You will need it.")
		human = X
		computer = O
	else:
		print("\nYour bravery will be your undoing... I will go first.")
		computer = X
		human = O
	return computer, human

def display_board(board):
	"""Display game board on screen."""
	print("\n\t", board[0], "|", board[1], "|", board[2])
	print("\t", "---------")
	print("\t", board[3], "|", board[4], "|", board[5])
	print("\t", "---------")
	print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
	"""Returns the empty squares."""
	moves = []
	for square in range(NUM_SQUARES):
		if board[square] in NUMBERS:
			moves.append(square)
	return moves

def winner(board):
	"""Determine the game winner."""
	WAYS_TO_WIN = ((0, 1, 2),
	(3, 4, 5),
	(6, 7, 8),
	(0, 3, 6),
	(1, 4, 7),
	(2, 5, 8),
	(0, 4, 8),
	(2, 4, 6))
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] not in NUMBERS:
			winner = board[row[0]]
			return winner
	if bool(set(NUMBERS) & set(board)) == False:
		return TIE
	return None

def human_move(board, human):
	"""Get human move."""
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
		if move not in legal:
			print("\nThat square is already occupied, foolish human. Choose another.\n")
	print("Fine...")
	return move

def computer_move(board, computer, human):
	"""Make computer move."""
	# make a copy to work with since function will be changing list
	board = board[:]
	# the best positions to have, in order
	BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
	print("I shall take square number", end=" ")
	# if computer can win, take that move
	for move in legal_moves(board):
		temp = board[move]
		board[move] = computer
		if winner(board) == computer:
			print(move)
			return move
		# done checking this move, undo it
		board[move] = temp

	# if human can win, block that move
	for move in legal_moves(board):
		temp = board[move]
		board[move] = human
		if winner(board) == human:
			print(move)
			return move
		# done checking this move, undo it
		board[move] = temp
	# since no one can win on next move, pick best open square
	for move in BEST_MOVES:
		if move in legal_moves(board):
			print(move)
			return move

def next_turn(turn):
	"""Switch turns."""
	if turn == X:
		return O
	else:
		return X

def congrat_winner(the_winner, computer, human):
	"""Congratulate the winner."""
	if the_winner != TIE:
		print(the_winner, "won!\n")
	else:
		print("It's a tie!\n")
	
	if the_winner == computer:
		print("As I predicted, human, I am triumphant once more. \n" \
			"Proof that computers are superior to humans in all regards.")
	elif the_winner == human:
		print("No, no!	 It cannot be!	 Somehow you tricked me, human. \n" \
			"But never again!	 I, the computer, so swear it!")
	else:
		print("You were most lucky, human, and somehow managed to tie me. \n" \
			"Celebrate today... for this is the best you will ever achieve.")

if __name__ == '__main__':
	display_instruct()
	computer, human = pieces() # 'x', 'o' or 'o', 'x'
	turn = X
	board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
	display_board(board)

	while not winner(board):
		if turn == human:
			move = human_move(board, human)
			board[move] = human
		else:
			move = computer_move(board, computer, human)
			board[move] = computer
		display_board(board)
		turn = next_turn(turn)

	the_winner = winner(board)
	congrat_winner(the_winner, computer, human)
	input("\n\nPress the enter key to quit.")
