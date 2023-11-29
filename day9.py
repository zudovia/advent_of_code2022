from copy import deepcopy

def move(grid, direction, count):
	grid_copy = deepcopy(grid)	

	for i in range(count):
		grid_copy = move_head(grid_copy, direction)
		grid_copy = move_tail(grid_copy)

	return grid_copy

def move_head(grid, direction):
	x, y = get_head_position(grid)

	match direction:

		case 'L':
			new_x = x - 1
			new_y = y

		case 'R':
			new_x = x + 1
			new_y = y

		case 'U':
			new_x = x
			new_y = y + 1

		case 'D':
			new_x = x
			new_y = y - 1

		case _:
			print(f'something went wrong: {direction}')

	new_grid = init_grid(len(grid), len(grid[0]), (new_x, new_y))
	new_grid[new_x][new_y] = 'H'

	return new_grid

def init_grid(deep, length, coordinates_head):
	if deep < coordinates_head[1]:
		new_deep = coordinates_head[1]
	else:
		new_deep = deep

	if length < coordinates_head[0]:
		new_length = coordinates_head[0]
	else:
		new_length = length

	grid = [['.'] * new_length] * new_deep

	return grid

def move_tail(grid):
	h_x, h_y = get_head_position(grid)
	t_x, t_y = get_tail_position(grid)

	if t_y == h_y:
		if t_x == h_x or t_x + 1 == h_x or t_x - 1 == h_x: 
			return grid
		else:
			new_grid = deepcopy(grid)
			new_grid[t_y][t_x] = '.'
			if t_x < h_x:
				new_grid[t_y][h_x - 1] = 'T'
			else:
				new_grid[t_y][h_x + 1] = 'T'
			return new_grid
	else:
		if t_x + 1 == h_x or n
		new_grid = deepcopy(grid)
		new_grid[t_y][t_x] = '.'
		if t_x == h_x:
			if t_y < h_y:
				new_grid[t_y][h_x + 1] = 'T'
			else:
				new_grid[t_y][h_x - 1] = 'T'
		elif t_x < h_x:





def get_head_position(grid):
	x, y = 0, 0
	return [x, y]

def get_tail_position(grid):
		x, y = 0, 0
	return [x, y]

def count_tail_position(grid):
	x, y = get_tail_position(grid)
	return f'{x}+{y}'

with open("input9.txt") as f:
	moves = []
	grid = []
	for line in f.read().splitlines():
		a, b = line.split(" ")
		moves.append([a, b])

	tail_positions = []
	for direction, count in moves:
		grid = move(grid, direction, int(count))
		tails_positions.append(count_tail_position(grid))

	tail_positions_set = set(tail_positions)
	print(len(tails_positions))