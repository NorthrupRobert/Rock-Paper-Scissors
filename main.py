# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep

import random
import rpsgraphics as g



BEST_OF = 3

victory, defeat = False, False
wins, losses = 0, 0
random.seed()

g.TitleScreen()

while not victory and not defeat:
	g.clear()
	g.rrd()
	computer_choice = random.choice(['R', 'S', 'P']) #computer randomly selects sign
	win = False

	print()
	user_choice = input("What are you playing?: ")
	temp = user_choice[0].upper()

	g.clear()
	g.prep()
	
	if (temp == computer_choice):
		if (temp == 'R'):
			g.rrd()
		elif (temp == 'S'):
			g.ss()
		elif (temp == 'P'):
			g.pp()
		print()
		print("=Tie!")
		
	elif (temp == 'R' or temp == 'S' or temp == 'P'): #valid response
		if (temp == 'R'):
			if(computer_choice == 'S'):
				win = True
				g.rs()
			else:
				g.rp()
				pass
		elif (temp == 'S'):
			if (computer_choice == 'P'):
				g.sp()
				win = True
			else:
				g.sr()
				pass
		elif (temp == 'P'):
			if (computer_choice == 'R'):
				g.pr()
				win = True
			else:
				g.ps()
				pass

		if (win == True):
			print()
			print("=You got one!")
			wins += 1
		else:
			print()
			print("=You lost one!")
			losses += 1

		if (((BEST_OF // 2) + 1) == wins):
			victory = True
		elif (((BEST_OF // 2) + 1) == losses):
			defeat = True
	
	else:
		print()
		print("=Response was out of bounds, try again!")
	
	print(f"=SCORE: {wins}/{losses}")
	
	sleep(5)

if (victory):
	print("Yay, you win! :D")
else:
	print("Awww shucks, better luck next time . . . :(")
		