
def get_pieces_from_file(filename, separator):
	"""
	opens file with pieces in format
	length; number

	returns list with all elements
	"""	
	elements = open(filename)

	pieces = []

	line = elements.readline()
	while line:
		temp = line.split(separator)
		length = float(temp[0])
		num = int(temp[1])

		for _ind in range(num):
			pieces.append(length)

		line = elements.readline()

	return pieces

def gen_combis(pieces, pallet_len):
	"""
	get list of all pieces and
	generates all possible combinations of different length
	"""
	first = pieces[0]
	rest = pieces[1:]

	if rest:
		acc = gen_combis(rest, pallet_len)
		new_acc = acc[:]

		for combi in acc:
			if sum(combi + [first]) < pallet_len:
				new_acc.append(combi + [first])
			temp = combi[:]
			for i in range(len(combi)):
				new_combi = temp.insert(i,first)
				if new_combi and sum(new_combi) < pallet_len:
					new_acc.append(new_combi)
		new_acc.append([first])
		return new_acc

	else:
		return [[first]]


elem = get_pieces_from_file('elements.txt',';')
# gen_combis(elem)

print '-'*40
print elem
print '-'*40

for line in gen_combis(elem, 6):
	print line