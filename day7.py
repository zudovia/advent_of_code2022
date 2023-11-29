import re

MEMORY_SIZE = 70000000
UPDATE_SIZE = 30000000

def get_count_size(k, dic):
	values = dic[k]
	sum = 0
	for v in values:
		splited = v.split(' ')
		if splited[0] == 'dir':
			if k == '/' or k[1] != "/":
				sum += get_count_size(f"/{k}{splited[1]}/", dic)
			else:
				sum += get_count_size(f"{k}{splited[1]}/", dic)
		else:
			sum += int(v.split(' ')[0])

	return sum

def get_path_folder(folder, path):
	folder_cleaning = folder.replace('$ cd ', '')
	folder_clean = folder_cleaning.replace('\n', '')

	if folder_clean == '/':
		return folder_clean
	else:
		path_folder = "/".join(path)

	return f"{path_folder}/{folder_clean}/"

def print_dic(dic):
	for key, value in dic.items():
		print(key, ': ', value, '\n')

with open("input7.txt") as f:

	content = f.readlines()
	content.append(' ')

	actual_path = []
	dic_tree = {}
	for i in range(len(content)):
		if content[i].startswith('$ cd'):
			folder_moving = content[i].replace('$ cd ', '')
			if folder_moving == '..\n':
				del actual_path[-1]
			else:
				actual_path.append(folder_moving.replace('\n', ''))

		if content[i] == '$ ls\n':
			for j in range(i+1, len(content)):
				if content[j][0] == '$':
					break
			key = get_path_folder(content[i-1], actual_path[:-1])
			value = []
			for k in range(i+1, j):
				value.append(content[k].replace('\n', '')) 
			dic = {key: value}
			dic_tree.update(dic)
 
	dic_results = {}
	for k in dic_tree.keys():
		dic_results.update({k: get_count_size(k, dic_tree)})

	unused_space = MEMORY_SIZE - dic_results['/']
	need_space =   UPDATE_SIZE - unused_space
	candidates = []
	for v in dic_results.values(): 
		if v > need_space:
			candidates.append(v)

	print(min(candidates))

	# sum_final = 0
	# for k, v in dic_results.items():


	# 	if k != '/' and v <= 100000:
	# 		sum_final += v
	# print(sum_final)



