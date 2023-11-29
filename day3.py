def split_items(line):
	middle = int((len(line))/2)
	end = int(len(line))
	a, b = line[:middle], line[middle:end] 
	return a, b

def get_priority(letter):
	priorities=  {x: ord(x) - 96 for x in 'abcdefghijklmnopqrstuvwxyz'}
	priorities_major = {x: ord(x) - 38 for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
	priorities.update(priorities_major) 
	return priorities[letter]

def get_prior_of_line(lines):
	a, b, c = lines[0], lines[1], lines[2]
	common = []
	sum = 0

	for i in a:
		if i in b and i in c and not i in common:
			common.append(i)

	for i in common:
		sum += get_priority(i)
	return sum


with open("input3.txt") as f:

	content = f.readlines()

	sum = 0
	i = 1
	lines_to_count = []

	for line in content:
		line = line.replace("\n", "")
		lines_to_count.append(line)

		if i < 3:
			i+=1
		else:
			sum += get_prior_of_line(lines_to_count)
			i = 1
			lines_to_count.clear()

	print(sum)


