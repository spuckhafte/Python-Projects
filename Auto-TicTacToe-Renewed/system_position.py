import random

#completing winning row
def win(v, oLoc, xLoc, options, locations):
	if v[1]==v[2]=="o" and v[3] not in options :
		oLoc = 3
	elif v[1]==v[3]=="o" and v[2] not in options :
		oLoc = 2
	elif v[2]==v[3]=="o" and v[1] not in options :
		oLoc = 1

	elif v[4]==v[5]=="o" and v[6] not in options :
		oLoc = 6
	elif v[4]==v[6]=="o" and v[5] not in options :
		oLoc = 5
	elif v[5]==v[6]=="o" and v[4] not in options :
		oLoc = 4

	elif v[7]==v[8]=="o" and v[9] not in options :
		oLoc = 9
	elif v[7]==v[9]=="o" and v[8] not in options :
		oLoc = 8
	elif v[8]==v[9]=="o" and v[7] not in options :
		oLoc = 7

	elif v[1]==v[4]=="o" and v[7] not in options :
		oLoc = 7
	elif v[1]==v[7]=="o" and v[4] not in options :
		oLoc = 4
	elif v[4]==v[7]=="o" and v[1] not in options :
		oLoc = 1

	elif v[2]==v[5]=="o" and v[8] not in options :
		oLoc = 8
	elif v[2]==v[8]=="o" and v[5] not in options :
		oLoc = 5
	elif v[5]==v[8]=="o" and v[2] not in options :
		oLoc = 2

	elif v[3]==v[6]=="o" and v[9] not in options :
		oLoc = 9
	elif v[3]==v[9]=="o" and v[6] not in options :
		oLoc = 6
	elif v[6]==v[9]=="o" and v[3] not in options :
		oLoc = 3

	elif v[1]==v[5]=="o" and v[9] not in options :
		oLoc = 9
	elif v[1]==v[9]=="o" and v[5] not in options :
		oLoc = 5
	elif v[5]==v[9]=="o" and v[1] not in options :
		oLoc = 1

	elif v[3]==v[5]=="o" and v[7] not in options :
		oLoc = 7
	elif v[3]==v[7]=="o" and v[5] not in options :
		oLoc = 5
	elif v[5]==v[7]=="o" and v[3] not in options :
		oLoc = 3

	#logics for continuing the game by breaking the triplets of player if possible
	elif v[1]==v[2]=="x" and v[3] not in options :
		oLoc = 3
	elif v[1]==v[3]=="x" and v[2] not in options :
		oLoc = 2
	elif v[2]==v[3]=="x" and v[1] not in options :
		oLoc = 1

	elif v[4]==v[5]=="x" and v[6] not in options :
		oLoc = 6
	elif v[4]==v[6]=="x" and v[5] not in options :
		oLoc = 5
	elif v[5]==v[6]=="x" and v[4] not in options :
		oLoc = 4

	elif v[7]==v[8]=="x" and v[9] not in options :
		oLoc = 9
	elif v[7]==v[9]=="x" and v[8] not in options :
		oLoc = 8
	elif v[8]==v[9]=="x" and v[7] not in options :
		oLoc = 7

	elif v[1]==v[4]=="x" and v[7] not in options :
		oLoc = 7
	elif v[1]==v[7]=="x" and v[4] not in options :
		oLoc = 4
	elif v[4]==v[7]=="x" and v[1] not in options :
		oLoc = 1

	elif v[2]==v[5]=="x" and v[8] not in options :
		oLoc = 8
	elif v[2]==v[8]=="x" and v[5] not in options :
		oLoc = 5
	elif v[5]==v[8]=="x" and v[2] not in options :
		oLoc = 2

	elif v[3]==v[6]=="x" and v[9] not in options :
		oLoc = 9
	elif v[3]==v[9]=="x" and v[6] not in options :
		oLoc = 6
	elif v[6]==v[9]=="x" and v[3] not in options :
		oLoc = 3

	elif v[1]==v[5]=="x" and v[9] not in options :
		oLoc = 9
	elif v[1]==v[9]=="x" and v[5] not in options :
		oLoc = 5
	elif v[5]==v[9]=="x" and v[1] not in options :
		oLoc = 1

	elif v[3]==v[5]=="x" and v[7] not in options :
		oLoc = 7
	elif v[3]==v[7]=="x" and v[5] not in options :
		oLoc = 5
	elif v[5]==v[7]=="x" and v[3] not in options :
		oLoc = 3
	else:
		pass

	return oLoc


#logic for easy game
def system_logic_easy(v, options, xLoc, oLoc, i, locations):
	#logic for random move as the game is neutral
	oLoc = random.choice(locations)
	pass

	#logic for double checking if the position of 'o' overlaps occupied grid
	if v[oLoc] == "o" or v[oLoc] == "x":
		oLoc = random.choice(locations)
	else:
		pass

	return oLoc

#logic for medium game if system starts first
def system_logic_medium_first(v, options, xLoc, oLoc, i, locations):
	if i==1:
		oLoc = random.choice([5, 1, 3, 7, 9])

	if i==2:
		if v[5] == "o":
			while True:
				system_case_ = [1,3,7,9]
				oLoc = random.choice(system_case_)
				if v[oLoc]=="x":
					continue
				else:
					break

		else:
			while True:
				if v[1]=="o" or v[3]=="o" or v[7]=="o" or v[9]=="o":

					if v[1]=="o" or v[9]=="o":
						oLoc = random.choice([3,7])
						if v[oLoc]=="x":
							continue
						else:
							break

					if v[3]=="o" or v[7]=="o":
						oLoc = random.choice([1,9])
						if v[oLoc]=="x":
							continue
						else:
							break
		
	#logic for random move as the game is neutral
	if i!=1 and i!=2:
		oLoc = random.choice(locations)
		pass

	return oLoc

#logic for medium game if system plays second
def system_logic_medium_second(v, options, xLoc, oLoc, i, locations):
	#logics for special moves leading towards tie
	if i==2:
		while True:
			system_case_ = [2,8,4,6]
			oLoc = random.choice(system_case_)
			if v[oLoc] not in options:
				break 
			else:
				continue
	
	#logic for random move as the game is neutral
	if i!=2:
		oLoc = random.choice(locations)
		pass

	#logic for double checking if the position of 'o' overlaps occupied grid
	if v[oLoc] == "o" or v[oLoc] == "x":
		oLoc = random.choice(locations)
	else:
		pass

	return oLoc

#logic for hard game if system starts first
def system_logic_hard_first(v, options, xLoc, oLoc, i, locations):
	#logics for special moves leading towards tie
	if i==1:
		oLoc = random.choice([5, 1, 3, 7, 9])

	if i==2:
		if v[5] == "o":
			while True:
				system_case_ = [1,3,7,9]
				oLoc = random.choice(system_case_)
				if v[oLoc]=="x":
					continue
				else:
					break

		else:
			while True:
				if v[1]=="o" or v[3]=="o" or v[7]=="o" or v[9]=="o":

					if v[1]=="o" or v[9]=="o":
						oLoc = random.choice([3,7])
						if v[oLoc]=="x":
							continue
						else:
							break

					if v[3]=="o" or v[7]=="o":
						oLoc = random.choice([1,9])
						if v[oLoc]=="x":
							continue
						else:
							break

	if i==3:
		if v[5] == "o":
			while True:
				if v[1]=="o" or v[9] == "o":
					oLoc = random.choice([3,7])
					if v[oLoc]=="x":
							continue
					else:
						break


				if v[3]=="o" or v[7] == "o":
					oLoc = random.choice([1,9])
					if v[oLoc]=="x":
							continue
					else:
						break
		else:
			while True:
				if v[1]==v[3]=="o":
					oLoc = random.choice([7,9])
					if v[oLoc]=="x" or v[oLoc] == "o":
						continue
					else:
						break
				if v[3]==v[9]=="o":
					oLoc = random.choice([1,7])
					if v[oLoc]=="x" or v[oLoc] == "o":
						continue
					else:
						break
				if v[9]==v[7]=="o":
					oLoc = random.choice([1,3])
					if v[oLoc]=="x" or v[oLoc] == "o":
						continue
					else:
						break
				if v[7]==v[1]=="o":
					oLoc = random.choice([3,9])
					if v[oLoc]=="x":
						continue
					else:
						break
	
	#logic for random move as the game is neutral
	if i!=1 and i!=2 and i!=3:
		oLoc = random.choice(locations)
		pass

	return oLoc

#logic for hard game if system plays second
def system_logic_hard_second(v, options, xLoc, oLoc, i, locations):
	#logics for special moves leading towards tie
	if i==1:
		if xLoc == 5:
			oLoc = random.choice([7,3])
		else:
			oLoc = 5

	if i==2:
		while True:
			if v[7] == "o" or v[3] == "o" :
				_system_case_ = [1,9]
				oLoc = random.choice(_system_case_)
				break

			else:
				system_case_ = [2,8,4,6]
				oLoc = random.choice(system_case_)
				if v[oLoc] not in options:
					break 
				else:
					continue
		
	#logic for random move as the game is neutral
	if i!=1 and i!=2:
		oLoc = random.choice(locations)
		pass

	#logic for double checking if the position of 'o' overlaps occupied grid
	if v[oLoc] == "o" or v[oLoc] == "x":
		oLoc = random.choice(locations)
	else:
		pass

	return oLoc
