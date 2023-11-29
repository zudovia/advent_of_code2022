from operator import countOf
from copy import deepcopy

crates_count = 9
max_in_one_crate_at_beginning = 8
start_read_move = 10

def get_draw(content):
	draw = []
	for i in range(crates_count):
		draw.append([])

	for j in range(crates_count-1):
		for k in range(max_in_one_crate_at_beginning + 1, 0, -1):
			draw[k-1].append(content[j][k-1])

	# print_draw(draw)
	final_draw = []
	for i in draw:
		for j in range(countOf(i, ' ')):
			i.remove(' ')
		i.reverse()
		final_draw.append(i)
	return final_draw

def get_moves(content):
	tab = []
	for move in content:
		move = move.replace('move ', '')
		move = move.replace('from ', '')
		move = move.replace('to ', '')
		move = move.replace('\n', '')

		tab.append(move.split(' '))

	return tab
	 
def print_draw(draw):
	for line in draw:
		print(line)

def input_to_tab(content):
	tab = []
	for i in content:
		tab.append(get_line_to_tab(i))
	return tab

def get_line_to_tab(line):
	length = len(line)
	tab = []
	for i in range(1, length, 4):
		tab.append(line[i])
	return tab

def move_two(draw, move):
	to_move = draw[int(move[1])-1][-1*int(move[0]):]
	for i in to_move:
		to_inverse = deepcopy(draw[int(move[1])-1])
		to_inverse.reverse()
		to_inverse.remove(i)
		to_inverse.reverse()
		draw[int(move[1])-1] = deepcopy(to_inverse)
	draw[int(move[2])-1] = draw[int(move[2])-1] + to_move
	return draw

def move_one(draw, move):
	to_move = draw[int(move[1])-1][-1*int(move[0]):]
	to_move.reverse()
	for i in to_move:
		to_inverse = deepcopy(draw[int(move[1])-1])
		to_inverse.reverse()
		to_inverse.remove(i)
		to_inverse.reverse()
		draw[int(move[1])-1] = deepcopy(to_inverse)
		draw[int(move[2])-1].append(i)
	return draw

def get_result(draw):
	result = ""
	for i in draw:
		result+=(i[-1] if i else '-')
	return result

with open("input5.txt") as f:
	content = f.readlines()
	
	tab = input_to_tab(content[:crates_count])
	draw = get_draw(tab)

	moves = get_moves(content[start_read_move:])

	for i in moves:
		draw = move_two(draw, i)
		print(i)
		print_draw(draw)
		print(" ")

	print(get_result(draw))

