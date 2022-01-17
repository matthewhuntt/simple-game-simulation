import random
import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats


class Player:
	def __init__(self, name, coins=4):
		self.name = name
		self.coins = coins

class Pot:
	def __init__(self, coins=2):
		self.coins = coins

class Game:
	def __init__(self, alternate):
		self.alternate = alternate
		self.cycles = 0
		self.over = False

def run_turn(player, pot, game):
	"""
	Runs a single turn. Rolls the die for the proved player and performs the required action.
	Returns False if the game is over, True otherwise
	"""

	#roll the die
	roll = random.randint(1, 6)

	#execute coin exchanges based on game rules
	if game.alternate == 3:
		if roll == 1:
			pot.coins += player.coins
			player.coins = 0

	if roll == 2:
		player.coins += pot.coins
		pot.coins = 0

	if roll == 3:
		player.coins += math.floor(pot.coins / 2)
		pot.coins -= math.floor(pot.coins / 2)

	if game.alternate == 4:
		if (roll == 4 or roll == 5):
			player.coins -= 1
			pot.coins += 1
	else:
		if (roll == 4 or roll == 5 or roll == 6):
			player.coins -= 1
			pot.coins += 1

	if player.coins < 0:
		game.over = True

def run_cycle(a, b, pot, game):
	"""
	Performs a cycle of the game with each player making a move
	"""
	
	run_turn(a, pot, game)
	run_turn(b, pot, game)

def run_game(alternate):
	"""
	Runs an entire game to completion and reports the number of cycles
	Returns a tuple with the number of cycles and the winner
	"""

	#initialize the players and pot
	if alternate == 1:
		player_a = Player('a', 5)
		player_b = Player('b')
		pot = Pot()

	elif alternate == 2:
		player_a = Player('a', 8)
		player_b = Player('b', 8)
		pot = Pot(4)

	else:
		player_a = Player('a')
		player_b = Player('b')
		pot = Pot()

	#initialize the game
	game = Game(alternate)

	#run cycles until the game is over
	while game.over == False:
		game.cycles += 1
		run_cycle(player_a, player_b, pot, game)

	#report the game's winner
	if player_a.coins > player_b.coins:
		return((game.cycles, player_a))
	else:
		return((game.cycles, player_b))

def main(args):
	n = int(args[1])
	a_win_count = 0
	cycles_list = []

	#set the seed if seed parameter is provided
	if len(args) >= 3:
		random.seed(args[2])

	#assign alternate version parameter 
	if len(args) == 4:
		alternate = int(args[3])
	else:
		alternate = 0

	#run n trials of the game
	for i in range(n):
		cycles, winner = run_game(alternate)
		cycles_list.append(cycles)
		if winner.name == 'a':
			a_win_count += 1

	#print basic statistics
	print("Mean Number of Cycles: " + str(np.mean(cycles_list)))
	print("Median Number of Cycles: " + str(np.median(cycles_list)))
	print("Most Common Number of Cycles: " + str(stats.mode(cycles_list)[0][0]))
	print("Longest Game: " + str(np.max(cycles_list)))
	print("Player A Winning Percentage: " + str(a_win_count / len(cycles_list)))

	#fit results
	#results = fit_results(cycles_list)

	#plot results
	p = sns.histplot(cycles_list, binwidth=1, kde=True)
	p.set_xlabel('Cycles Required for Game to Terminate')
	p.set_title('Cycle Distribution')
	plt.show()



if __name__ == '__main__':
    import sys
    main(sys.argv)





