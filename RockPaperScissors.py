import time
import random
print("\nROCK(R) PAPER(P) SCISSORS(S)")
print("Select your choice")
print("\n5 Rounds\n")

system_choice = ["r", "p", "s"]

visuals = {
	"r": "💎",
	"p": "📄",
	"s": "✂️",
}

rounds = 0
score_player = 0
score_system = 0 

while rounds<5:
	rounds+=1
	move_system = random.choice(system_choice)
	move_player = input("\nChoose: ").lower()

	if move_player == move_system:
		rounds-=1
		print(f"\nIts a Tie - Rounds Left: {5-rounds}")
		print(f'{visuals[move_player]} vs {visuals[move_system]}')


	if move_player == "r" and move_system == "s":
		print(f"\nPlayer wins over Computer - Rounds Left: {5-rounds}")
		score_player += 1
		print(f'{visuals[move_player]} vs {visuals[move_system]}')

	if move_player == "p" and move_system == "r":
		print(f"\nPlayer wins over Computer - Rounds Left: {5-rounds}")
		score_player += 1
		print(f'{visuals[move_player]} vs {visuals[move_system]}')

	if move_player == "s" and move_system == "p":
		print(f"\nPlayer wins over Computer - Rounds Left: {5-rounds}")
		score_player += 1
		print(f'{visuals[move_player]} vs {visuals[move_system]}')

	if move_player == "s" and move_system == "r":
		print(f"\nSystem wins over Player - Rounds Left: {5-rounds}")
		score_system += 1
		print(f'{visuals[move_system]} vs {visuals[move_player]}')

	if move_player == "r" and move_system == "p":
		print(f"\nSystem wins over Player - Rounds Left: {5-rounds}")
		score_system += 1
		print(f'{visuals[move_system]} vs {visuals[move_player]}')

	if move_player == "p" and move_system == "s":
		print(f"\nSystem wins over Player - Rounds Left: {5-rounds}")
		score_system += 1
		print(f'{visuals[move_player]} vs {visuals[move_system]}') 
		
	if move_player not in system_choice:
		rounds -= 1 
		continue

if score_system > score_player:
	print("\n----------------")
	print("\nComputer Wins")
	print(f"Score: {score_player}/{score_system}")
elif score_player > score_system:
	print("\n----------------")
	print("\nPlayer Wins")
	print(f"Score: {score_player}/{score_system}")
else:
	print("\n----------------")
	print("\nIts a Draw !")
	print(f"Score: {score_player}/{score_system}")
