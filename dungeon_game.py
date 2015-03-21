import random

CELLS = [(0, 0), (0, 1), (0, 2), (0, 3),
		 (1, 0), (1, 1), (1, 2), (1, 3),	
		 (2, 0), (2, 1), (2, 2), (2, 3),
		 (3, 0), (3, 1), (3, 2), (3, 3)]


def get_locations():
	# monster = random
	monster = random.choice(CELLS)
	# door = random
	door = random.choice(CELLS)
	# start = random
	start = random.choice(CELLS)

	# if monster, door, or start are the same, do it again
	if monster == door or monster == start or door == start:
		return get_locations()
	# return monster, door, start
	return monster, door, start


def move_player(player, move):
	# player = (x, y)
	# Get the player's current location
	x, y = player
	# If move is LEFT, y - 1
	if move == 'LEFT':
		y -= 1
	# If move is RIGHT, y + 1
	elif move == 'RIGHT':
		y += 1
	# If move is UP, x - 1
	elif move == 'UP':
		x -= 1
	# If move is DOWN, x + 1
	elif move == 'DOWN':
		x += 1

	return x, y

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	# player = (x, y)

	# If player's y is 0, remove LEFT
	if player[1] == 0:
		moves.remove('LEFT')
	# If player's y is 2, remove RIGHT
	if player[1] == 3:
		moves.remove('RIGHT')
	# If player's x is 0, remove UP
	if player[0] == 0:
		moves.remove('UP')
	# If player's x is 2, remove DOWN
	if player[0] == 3:
		moves.remove('DOWN')

	return moves


def draw_map(player, string):
	print(' _ _ _ _')
	tile = '|{}'
	for idx, cell in enumerate(CELLS):
		if idx in [3, 7, 11, 15]:
			if cell == player:
				print(tile.format('{}|'.format(string)))
			else:
				print(tile.format('_|'))
		else:
			if cell == player:
				print(tile.format('{}'.format(string)), end='')
			else:
				print(tile.format('_'), end='')

monster, door, player = get_locations()
print("Welcome to the dungeon!")

while True:
	moves = get_moves(player)

	print("You're currently in room {}".format(player)) # fill in with player position

	draw_map(player, 'X')

	print("You can move {}".format(moves)) # fill in with available moves
	print("Enter QUIT to quit")


	move = input("> ")
	move = move.upper()

	if move == 'QUIT':
		break

	# If it's a good move, change the player's position
	# If it's a bad move, dont change anything
	# If the new player position is the door, they win!
	# If the new player position is the monster, they lose!
	# Otherwise, continue
	if move in moves:
		player = move_player(player, move)
	else:
		print("** Walls are hard, stop walking into them! **")
		continue

	if player == door:
		draw_map(player, 'O')
		print("You're currently in room {}".format(player)) # fill in with player position
		print("You escaped!")
		break
	elif player == monster:
		draw_map(player, 'D') # 'D' represent Dead
		print("You're currently in room {}".format(player)) # fill in with player position
		print("You were eaten by the grue!")
		break





