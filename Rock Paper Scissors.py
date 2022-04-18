import random

#Setting the score to 0
score = 0

#Telling the user how to exit
print('Enter 0 to exit')

#Functions for if the user wins, loses, or ties
class win_lose_tie:
	def __init__(self):
		pass
	def win():
		global score
		score +=1
		print('The computer got: ' + computer_move + ', you won')
		print(str(score))
	def lose():
		global score
		score -=1
		print('The computer got: ' + computer_move + ', you lost')
		print(str(score))
	def tie():
		global score
		print('The computer got: ' + computer_move + ', you tied')
		print(str(score))


while True:
	#Computer getting rock, paper, or scissors
	def turn():
		move = ''
		n = random.randint(0,2)
		if n == 0:
			move = 'Rock'
		elif n == 1:
			move = 'Scissors'
		else:
			move = 'Paper'

		return move

	#Setting the computers move to a variable
	computer_move = turn()

	#Asking the user for their move
	user_move = input('Rock, Paper or Scissors?: ')

	#Checking to see if the user won, lost or tie
	if user_move == computer_move:
		win_lose_tie.tie()
	elif user_move == 'Rock' and computer_move == 'Paper':
		win_lose_tie.lose()
	elif user_move == 'Rock' and computer_move == 'Scissors':
		win_lose_tie.win()
	elif user_move == 'Paper' and computer_move == 'Rock':
		win_lose_tie.win()
	elif user_move == 'Paper' and computer_move == 'Scissors':
		win_lose_tie.lose()
	elif user_move == 'Rock' and computer_move == 'Paper':
		win_lose_tie.lose()
	elif user_move == 'Rock' and computer_move == 'Scissors':
		win_lose_tie.win()
	elif user_move == '0':
		break
	else:
		print('Please enter a valid move')

