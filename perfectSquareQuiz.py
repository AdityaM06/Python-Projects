import random

#The maxium number 
up_to = 25

#Global Variables
list_of_no = []
no_to_guess = 0
list_of_wrong = []
user_guess = ''

#Making a list that has all the numbers from 1 to 'up_to'
for i in range(1,up_to+1):
	list_of_no.append(i)

#Asks user for an input
def get_input():
    global user_guess
   	#Making sure the user types an integer
    try:
	    user_guess = int(input('What is ' + str(no_to_guess) + ' squared?: '))
    except:
        print('Please enter only an integer')
        get_input()

#Picks a random number from the list of numbers from 1 to 'up_to'
def get_number_to_square():
		global no_to_guess

		indx = random.randint(0,len(list_of_no)-1)
		no_to_guess = list_of_no[indx]
		list_of_no.pop(indx)
    
#Loops until no numbers are left
while len(list_of_no) > 0:
	
	get_number_to_square()
	get_input()
    
	#Checking to see if the users answer was right
	if user_guess == no_to_guess**2:
		print('Correct')
	elif user_guess != no_to_guess**2:
		print('Incorrect, readding number to sequence')
		#Adds back the wrong guess so the user can try again
		list_of_no.append(no_to_guess)
		#Keeps track of the numbers the user didn't get right in the first time
		list_of_wrong.append(no_to_guess)

print('You got all the squares!')
#Prints if the user didnt answer correctly on the first try
if len(list_of_wrong) > 0:
	print('You got these ones wrong')
	print(list_of_wrong)
