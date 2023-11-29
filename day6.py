from operator import countOf

def is_marker(str):
	for i in range(len(str)):
		if countOf(str, str[i]) > 1:
			return False

	return True

def is_message(str):
	for i in range(len(str)):
		if countOf(str, str[i]) > 1:
			return False

	return True

with open("input6.txt") as f:
	content = f.read()
	dic_marker = {i: content[i-4:i] for i in range(4, len(content))}
	
	for k, v in dic_marker.items():
		if is_marker(v):
			marker = k
			break

	dic_message = {i: content[i-14:i] for i in range(marker, len(content))}
	for k, v in dic_message.items():
		if is_message(v):
			message = k
			break

	f.close()

print(message)


