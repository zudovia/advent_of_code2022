def get_visible_on_the_interior(content):
	sum = 0
	for x in range(1, len(content[0])-1):
		for y in range(1, len(content)-1):
			if is_visible_from_the_left(content, x, y) or is_visible_from_the_top(content, x, y) or is_visible_from_the_right(content, x, y) or is_visible_from_the_bottom(content, x, y):
				sum += 1
	return sum

def is_visible_from_the_left(content, x, y):
	for i in range(x):
		if content[y][i] >= content[y][x]:
			return False
	return True 

def is_visible_from_the_top(content, x, y):
	for i in range(y):
		if content[i][x] >= content[y][x]:
			return False
	return True  

def is_visible_from_the_right(content, x, y):
	for i in range(len(content[0])-1, x, -1):
		if content[y][i] >= content[y][x]:
			return False
	return True 

def is_visible_from_the_bottom(content, x, y):
	for i in range(len(content)-1, y, -1):
		if content[i][x] >= content[y][x]:
			return False
	return True 

def get_scenic_score(content):
	scores = []
	for x in range(1, len(content[0])-1):
		for y in range(1, len(content)-1):
			scores.append(get_visible_from_the_left(content, x, y) * get_visible_from_the_top(content, x, y) * get_visible_from_the_right(content, x, y) * get_visible_from_the_bottom(content, x, y))
	return max(scores)

def get_visible_from_the_left(content, x, y):
	count = 0
	for i in range(x - 1, -1, -1):
		if content[y][i] >= content[y][x]:
			count += 1
			return count
		else:
			count += 1
	return count

def get_visible_from_the_top(content, x, y):
	count = 0
	for i in range(y - 1, -1, -1):
		if content[i][x] >= content[y][x]:
			count += 1
			return count
		else:
			count += 1
	return count 

def get_visible_from_the_right(content, x, y):
	count = 0
	for i in range(x + 1, len(content[0])):
		if content[y][i] >= content[y][x]:
			count += 1
			return count
		else:
			count += 1
	return count

def get_visible_from_the_bottom(content, x, y):
	count = 0
	for i in range(y + 1, len(content)):
		if content[i][x] >= content[y][x]:
			count += 1
			return count
		else:
			count += 1
	return count

with open("input8.txt") as f:

	content = f.read().splitlines()

	visible_on_the_edge = len(content) * 2 + (len(content[0]) - 2) * 2

	visible_on_the_interior = get_visible_on_the_interior(content)

	# print(visible_on_the_edge + visible_on_the_interior)

	print(get_scenic_score(content))
	
