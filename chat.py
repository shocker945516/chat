def read_txt(filename):
	data = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for i in f:
			data.append(i.strip())
	return data

def convert(lines):
	new_data = []
	person = None
	for i in lines:
		if i == 'Allen':
			person = 'Allen'
			continue
		elif i == 'Tom':
			person = 'Tom'
			continue
		if person:
			new_data.append(person + ': ' + i)
	return new_data

def output(filename, data):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for i in data:
			f.write(i + '\n')

def main():
	data = read_txt('input.txt')
	data = convert(data)
	output('output.txt', data)

main()