import random

secret_word = ''
user_guess = ''
dashes = ''
guesses = 0
no_of_guesses = 10
guessed = False

def print_rules():
	print('You have 10 chances to guess the secret word. Each \"-\" represents a letter in the alphabet. You will try to guess the word by guessing each letter')

print_rules()

def get_word():
	global secret_word
	global dashes
	
	word_list = ['train', 'car', 'bus', 'plane']
	corrospoinding_dashes = []

	for i in range(0,len(word_list)):
		corrospoinding_dashes.append('-'*len(word_list[i]))

	
	indx = random.randint(0,len(word_list)-1)

	dashes = corrospoinding_dashes[indx]
	secret_word = word_list[indx]

def get_guess():
	global user_guess
	global guesses
	user_guess = str(input('Please guess the next letter: '))
	
	if len(user_guess) != 1:
		print('Please write one charecter only')
		get_guess()
	elif not user_guess.isalpha():
		print('Please use a charecter of the alphabet')
		get_guess()
	elif user_guess.isalpha() and len(user_guess) == 1:
		
		if secret_word.count(user_guess) == 0:
			print('That letter is not in the word')
			guesses +=1
		elif secret_word.count(user_guess) >= 1:
			print('That letter is in the word')
		else:
			print('Something went wrong')
	else:
		print('Something went wrong, try again')
		get_guess()


def update_dashes():
	global secret_word
	global user_guess
	global dashes

	result = ''
	for i in range(0,len(secret_word)):
		if secret_word[i] == user_guess:
			result += user_guess
		else:
			result += dashes[i]
	
	dashes = result
	return result


get_word()
print(dashes)
while not guessed: 
	get_guess()
	print(update_dashes())
	
	if dashes.count('-') == 0:
		guessed = True
		print('Congrats, you won!')

	print('You have ' + str((10-guesses)) + ' guesses left')
	
	if guesses == no_of_guesses:
		print('You\'re out of guesses, you lose')
		print('The word was: ' + secret_word)
		break
	


print('The game is over')