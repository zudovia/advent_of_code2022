with open("input4.txt") as f:
	count = 0
	for line in f.read().splitlines():
		a, b = line.split(",")

		start1, end1 = a.split("-")
		start2, end2 = b.split("-")

		set1 = set(range(int(start1), int(end1)+1))
		set2 = set(range(int(start2), int(end2)+1))

		# if set1.issubset(set2) or set2.issubset(set1):
		# 	count += 1

		inter = set1.intersection(set2)

		if len(inter) != 0:
			count += 1

	print(count)