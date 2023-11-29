# A = rock, B = Paper, C = scissors
# X = rock = 1 pt, Y = Paper = 2 pts, Z = scissors = 3 pts
# lost = 0 pt, draw = 3 pts, won = 6 pts
# X = lose, Y = draw, Z = won

def get_points(key):

	points = {
		"A+X": "4",
		"B+X": "1",
		"C+X": "7",
		"A+Y": "8",
		"B+Y": "5",
		"C+Y": "2",
		"A+Z": "3",
		"B+Z": "9",
		"C+Z": "6",
	}

	return points[key]

def get_play(play_adverse, strategy):

	key = f"{play_adverse}+{strategy}" 

	points = {
		"A+X": "Z",
		"B+X": "X",
		"C+X": "Y",
		"A+Y": "X",
		"B+Y": "Y",
		"C+Y": "Z",
		"A+Z": "Y",
		"B+Z": "Z",
		"C+Z": "X",
	}

	return f"{play_adverse}+{points[key]}"


sum = 0
with open("input2.txt") as f:

	for line in f.read().splitlines():
		a, b = line.split(" ")
		play = get_play(a, b)
		pts = int(get_points(play))
		sum += pts

print(sum)
