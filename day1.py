calories_per_elf = []
sum = 0

with open("input1.txt") as f:
	content = f.readlines()

	for line in content:
		line = line.replace("\n", "")
		if line != "":
			sum += int(line)
		else:
			calories_per_elf.append(sum)
			sum = 0

max1 = max(calories_per_elf)
calories_per_elf.remove(max1)
max2 = max(calories_per_elf)
calories_per_elf.remove(max2)
max3 = max(calories_per_elf)

answer = max1 + max2 + max3

print(answer)




