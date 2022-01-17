The program die_game.py implements the following simple die-based game:


There are two players, A and B. At the beginning
of the game, each starts with 4 coins, and there are 2 coins in the pot. A goes first,
then B, then A,. . . . During a particular player’s turn, the player tosses a 6-sided
die. If the player rolls a:

•1, then the player does nothing.
•2: then the player takes all coins in the pot.
•3: then the player takes half of the coins in the pot (rounded down).
•4,5,6: then the player puts a coin in the pot.

A player loses (and the game is over) if they are unable to perform the task (i.e.,
if they have 0 coins and need to place one in the pot). We define a cycle as A and
then B completing their turns. The exception is if a player goes out; that is the
final cycle (but it still counts as the last cycle). 

____________________________________________________________________
The program can be run from the command line by passing 3 parameters:

1. The number of trials to be run
2. The random seed for the generator
3. The alternate version as defined below

Example: "$ python3 die_game.py 100000 1 0" will run the program with 100,000 trials, a random seed of 1, and using alternate 0 rules.

The output will be a histogram of the resulting number of cycles for each game in the trial, as well as a list of basic summary statistics

____________________________________________________________________
Alternate Versions:

0. Game as originally defined
1. Initialize player A with 5 coins to start while keeping player B at 4 coins.
2. Double the coins initialized to each of the players as well as the pot.
3. Instead of requiring no action, require players to place all of their coins in the pot if they
roll a 1.
4. Instead of assigning 3 die outcomes to the action requiring players to place one coin in the pot, assign only 2 outcomes. The third outcome will require no action.

