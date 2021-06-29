import sys
import random
import time

# Data for different levels of the 'game'
mode = {
	"e": "10",
	"eup": "50",
	"low": "1",
	"h": "5",
	"hup": "60"
	}

trial = 0
chance = 0

# first while-loop is repeat the program instead of terminating if the input is other than 'int'
while True:

	# this try-except couple checks the required correct input
	try:
		i=3
		print("\n---Guess the Number---")
		level = input('\nWhat level do you want (easy/hard): ').lower()

		# condition if the level is easy
		if("e" in level):
			print('Loading...')
			time.sleep(0.4)
			text = "[██████████████████████]"
			for char in text:
			    sys.stdout.write(char)
			    time.sleep(0.01)

			print("\n\nEASY MODE:")
			time.sleep(0.5)
			while i>0:
				print(str(i))
				time.sleep(1)
				i=i-1
			print("START !!!")
			print("\nGuess a number that can be anything from '"+mode.get("low")+" to "+mode.get("eup")+"', you have "+mode.get("e")+" chances !!!")

			# random number generation
			number = random.randint(int(mode.get("low")),int(mode.get("eup")))

			# while-loop: checks the required chances given in certain level
			while trial <= int(mode.get("e")):
				guess = input('\nChance '+str(trial+1)+'>> ')

				# condition for correct guess
				if(number == int(guess)):
					print('\nYou guessed the right number !')
					break

				# condition for incorrect guess
				else:

					# this number will be used to calculate the accuracy of the guess
					closeness = abs(number-int(guess))

					trial = trial+1
					trialsLeft = int(mode.get("e"))-trial
					if (trialsLeft != 0):
						if (closeness in range(1,4)):
							print("That's not correct. Try again, you are left with "+str(trialsLeft)+" out of "+mode.get("e")+" chances!")
							time.sleep(0.2)
							print("(you were really close)")
							continue
						elif (closeness in range(4,9)):
							print("That's not correct. Try again, you are left with "+str(trialsLeft)+" out of "+mode.get("e")+" chances!")
							time.sleep(0.2)
							print("(you were in a good range of the actual number)")
							continue
						else:
							print("That's not correct. Try again, you are left with "+str(trialsLeft)+" out of "+mode.get("e")+" chances!")
							time.sleep(0.2)
							print("(you were too far from the original number)")
							continue
					else:
						print('\nYou lost it, the number was: '+str(number))
						break
			break

		# condition if the level is hard
		elif("h" in level):
			print('Loading...')
			time.sleep(0.4)
			text = "[██████████████████████]"
			for char in text:
			    sys.stdout.write(char)
			    time.sleep(0.01)
			print("\n\nHARD MODE:")
			time.sleep(0.5)
			while i>0:
				print(str(i))
				time.sleep(1)
				i=i-1
			print("START !!!")
			print("\nGuess a number that can be anything from '"+mode.get("low")+" to "+mode.get("hup")+"', you have "+mode.get("h")+" chances !!!")

			# random number generation
			number = random.randint(int(mode.get("low")),int(mode.get("hup")))
			while trial <= int(mode.get("h")):
				guess = input('\nChance '+str(trial+1)+'>> ')

				# condition for correct guess
				if(number == int(guess)):
					print('\nYou guessed the right number !')
					break

				# conditon for incorrect guess
				else:

					# this number will be used to calculate the accuracy of the guess
					closeness = abs(number-int(guess))

					#outputting the accuracy and chances left
					trial = trial+1
					trialsLeft = int(mode.get("h"))-trial
					if (trialsLeft != 0):
						if (closeness in range(1,4)):
							print("That's not correct. Try again, you are left with "+str(trialsLeft)+" out of "+mode.get("h")+" chances!")
							time.sleep(0.2)
							print("(you were really close)")
							continue
						elif (closeness in range(4,9)):
							print("That's not correct. Try again, you are left with "+str(trialsLeft)+" out of "+mode.get("h")+" chances!")
							time.sleep(0.2)
							print("(you were in a good range of the actual number)")
							continue
						else:
							print("That's not correct. Try again, you are left with "+str(trialsLeft)+" out of "+mode.get("h")+" chances!")
							time.sleep(0.2)
							print("(you were too far from the original number)")
							continue
					else:
						print('\nYou lost it, the number was: '+str(number))
						break
			break

		# condition if the level selection command is wrong
		else:
			print('Wrong command, Try again!')
			continue
	except:
		print('\nThat was a wrong command !')
		continue
