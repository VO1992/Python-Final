import random

print("Welcome to my game!")

gamesWon = 0
gamesTotal = 0
play = True

while play == True:
	computer = random.choice(['rock', 'paper', 'scissors'])
	player = str(input("What do you want to be: "))
	print("The computer has " + computer)
	
	if player == 'paper' and computer == 'paper':
		print("IT'S A TIE!")
		gamesTotal = gamesTotal + 1
	elif player == 'paper' and computer == 'rock':
		print('YOU WIN!')
		gamesWon = gamesWon + 1
	elif player == 'paper' and computer == 'scissors':
		print('YOU LOSE!')
		gamesTotal = gamesTotal + 1
	
	elif player == 'rock' and computer == 'rock':
		print("IT'S A TIE!")
		gamesTotal = gamesTotal + 1
	
	elif player == 'rock' and computer == 'scissors':
		print("YOU WIN!")
		gamesWon = gamesWon + 1
		gamesTotal = gamesTotal + 1

	elif player == 'rock' and computer == 'paper':
		print('YOU LOSE!')
		gamesTotal = gamesTotal + 1

	elif player == 'scissors' and computer == 'scissors':
		print("IT'S A TIE!")
		gamesTotal = gamesTotal + 1

	elif player == 'scissors' and computer == 'rock':
		print('YOU LOSE!')
		gamesTotal = gamesTotal + 1

	elif player == 'scissors' and computer == 'paper':
		print('YOU WON!')
		gamesWon = gamesWon + 1

	if gamesTotal == 10:
		play = False
		break;

average = (gamesWon / gamesTotal) * 100
print('Your win percentage is: ' + str(average) + '%')


