from dataclasses import dataclass, field
from typing import List
import difflib

@dataclass
class Monkey:
	number: int
	test: int
	action: list[str] = field(default_factory=list)
	item: list[int] = field(default_factory=list)
	test_result: list[int] = field(default_factory=list)
	#[true, false]

	def do_test(self, worry_level: int):
		if worry_level % self.test == 0:
			return self.test_result[0]
		else:
			return self.test_result[1]

	def operation(self, worry_level: int):
		

		# return 

def read_input(monkey: List[int]):
	model = [
		"Monkey :",
		"  Starting items: ",
		"  Operation: ",
		"  Test: divisible by ",
		"    If true: throw to monkey ",
		"    If false: throw to monkey "]

	output_list = []

	for i in range(len(monkey)):
		output_list.append([j[-1] for j in difflib.ndiff(model[i], monkey[i]) if j.startswith('+') and j[-1] != ' '])

	starting_items = ""
	items = []
	for i in output_list[1]:
		starting_items += i
	items = [int(i) for i in starting_items.split(",")]
	# print(items)

	test = ""
	for i in output_list[3]:
		test += i
	# print(int(test))

	op_concat = ""
	for i in output_list[2]:
		op_concat += i
	operation = op_concat.replace("old", "x")
	operation = operation.replace("new=", "")



	Monkey(
		number=int(output_list[0]),
		item=items,
		test=int(test),
		test_result=[int(output_list[-2], output_list[-1])])

	# print(output_list)

with open("input11.txt") as f:
	monkeys = []
	content = f.read().splitlines()
	for i in [j for j in range(len(content)+1) if j%7  == 0]:
		read_input(content[i:i+6])
