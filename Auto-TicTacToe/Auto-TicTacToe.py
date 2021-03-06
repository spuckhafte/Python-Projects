import list_package as lp
import random
import time
import system_position

#values of the different positions
v = {
	1: " ",
	2: " ",
	3: " ", 
	4: " ", 
	5: " ",
	6: " ", 
	7: " ", 
	8: " ", 
	9: " "
}

#board showing allocation of different grids to certain number
board_chart = '''
|1|2|3|
|4|5|6|
|7|8|9|
'''
print("TICTACTOE - 60% end up with a Tie (in Hard Mode), can You win ?\n")

time.sleep(0.3)
level = input("\nChoose level: Easy/Medium/Hard(E/M/H): ").lower()
time.sleep(0.3)

time.sleep(1)
print("\nAssign the value of 'x' in a particlular grid by entering the allotted positon.")
print("(Type '0' anytime to get the board chart)\n")
print(board_chart)
time.sleep(0.5)

i=0

#locations available for player and system
locations=[1,2,3,4,5,6,7,8,9]

options = ["x", "o"]

while True:
	#this increment in 'i' is for checking 'Tie' situation
	i=i+1

	#Player's Turn: ----------------------
	while True:
		try:
			xLoc = int(input('\nx: '))
			if xLoc in locations:
				break
			elif xLoc == 0:
				print(board_chart)
			else:
				print("Invalid Input, Try Again")
				continue
		except:
			print("Invalid Input, Try Again")
			continue

	#Assigning x's position (player's positon)
	v[xLoc] = 'x'

	#this location gets removed from that list as it has been used
	locations.pop(lp.indexOf(locations, xLoc))

	#board showing x's position
	board = f'''
	|{v[1]}|{v[2]}|{v[3]}|
	|{v[4]}|{v[5]}|{v[6]}|
	|{v[7]}|{v[8]}|{v[9]}|
	'''
	print(board)

	#logic if there is a 'win' for x or a 'tie' or 'the game is still on'
	if(v[1]==v[2]==v[3]=="x" or v[4]==v[5]==v[6]=="x" or v[7]==v[8]==v[9]=="x" or v[1]==v[4]==v[7]=="x" or v[2]==v[5]==v[8]=="x" or v[3]==v[6]==v[9]=="x" or v[1]==v[5]==v[9]=="x" or v[3]==v[5]==v[7]=="x"):
		time.sleep(0.5)
		print("\nPlayer WINS !")
		time.sleep(2)
		break
	elif i==5:
		time.sleep(0.5)
		print("\nTIE")
		time.sleep(2)
		break
	else:
		pass

	#System's Turn: ----------------------
	oLoc=0

	# Function for getting the most approriate position for system (according to the level selected)
	if level == "easy" or level == "e":
		oLoc = system_position.system_logic_easy(v, options, xLoc, oLoc, i, locations)
	if level == "medium" or level == "m":
		oLoc = system_position.system_logic_medium(v, options, xLoc, oLoc, i, locations)
	if level == "hard" or level == "h":
		oLoc = system_position.system_logic_hard(v, options, xLoc, oLoc, i, locations)
		
	#final location of 'o' (system)
	v[oLoc] = 'o'

	board = f'''
	|{v[1]}|{v[2]}|{v[3]}|
	|{v[4]}|{v[5]}|{v[6]}|
	|{v[7]}|{v[8]}|{v[9]}|
	'''

	#interactive text for engaging the player
	time.sleep(0.5)
	print('\nComputer is thinking...')
	time.sleep(1.5)
	print(board)

	#logic to check if there is a 'win' or 'the game is still going on' for system
	if(v[1]==v[2]==v[3]=="o" or v[4]==v[5]==v[6]=="o" or v[7]==v[8]==v[9]=="o" or v[1]==v[4]==v[7]=="o" or v[2]==v[5]==v[8]=="o" or v[3]==v[6]==v[9]=="o" or v[1]==v[5]==v[9]=="o" or v[3]==v[5]==v[7]=="o"):
		time.sleep(0.5)
		print("\nComputer WINS !")
		time.sleep(2)
		break
	else:
		continue