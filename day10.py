def print_image(image, cycles):
	line = ""
	for i in range(240):
		if i not in cycles:
			line += image[i]
		else:
			line += image[i]
			print(line)
			line = ""
		# print(image[i])

with open("input10.txt") as f:
	x = [1]
	for line in f.read().splitlines():
		if "addx" in line:
			x.append(x[-1])
			x.append(x[-1] + int(line.split(" ")[1]))
		if "noop" in line:
			x.append(x[-1])

cycles = [20, 60, 100, 140, 180, 220]
# sum = 0
# for c in cycles:
# 	sum += (c * x[c-1])

# print(sum)

image = []
cycles_range = [i-1 for i in range(1,241) if i%40 == 0]
cycles_range_bis = [i for i in range(1,241) if i%40 == 0]

j = 0
for i in range(240):
	if i in cycles_range_bis:
		j = i
	if x[i]-1 <= i-j and x[i]+2 > i-j:
		image.append("#")
	else:
		image.append(".")

print_image(image, cycles_range)