import time
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

board_chart = '''
|1|2|3|
|4|5|6|
|7|8|9|
'''
print("TICTACTOE\n")

time.sleep(1)
print("Assign the value of 'x' in a particlular grid by entering the allotted Positon: \n")
print(board_chart)
time.sleep(0.5)

i=0

locations = [1,2,3,4,5,6,7,8,9]
while True:
	i=i+1
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

	v[xLoc] = 'x'
	locations.remove(xLoc)

	board = f'''
	|{v[1]}|{v[2]}|{v[3]}|
	|{v[4]}|{v[5]}|{v[6]}|
	|{v[7]}|{v[8]}|{v[9]}|
	'''
	print(board)

	if(v[1]==v[2]==v[3]=="x" or v[4]==v[5]==v[6]=="x" or v[7]==v[8]==v[9]=="x" or v[1]==v[4]==v[7]=="x" or v[2]==v[5]==v[8]=="x" or v[3]==v[6]==v[9]=="x" or v[1]==v[5]==v[9]=="x" or v[3]==v[5]==v[7]=="x"):
		time.sleep(0.5)
		print("\nX WINS !")
		time.sleep(2)
		break
	elif i==5:
		time.sleep(0.5)
		print("\nTIE")
		time.sleep(2)
		break
	else:
		pass

	while True:
		try:
			oLoc = int(input('\no: '))
			if oLoc in locations:
				break
			elif oLoc == 0:
				print(board_chart)
			else:
				print("Invalid Input, Try Again")
				continue
		except:
			print("Invalid Input, Try Again")
			continue

	v[oLoc] = 'o'
	locations.remove(oLoc)
	
	board = f'''
	|{v[1]}|{v[2]}|{v[3]}|
	|{v[4]}|{v[5]}|{v[6]}|
	|{v[7]}|{v[8]}|{v[9]}|
	'''
	print(board)

	if(v[1]==v[2]==v[3]=="o" or v[4]==v[5]==v[6]=="o" or v[7]==v[8]==v[9]=="o" or v[1]==v[4]==v[7]=="o" or v[2]==v[5]==v[8]=="o" or v[3]==v[6]==v[9]=="o" or v[1]==v[5]==v[9]=="o" or v[3]==v[5]==v[7]=="o"):
		time.sleep(0.5)
		print("\nO WINS !")
		time.sleep(2)
		break
	else:
		continue
