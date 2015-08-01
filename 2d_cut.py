
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

	elements.close()

	return pieces

def gen_pallets(pieces, pallet_len):
	"""
	get list of all pieces and
	generates all possible combinations of different length
	returns list of conbis (list)
	"""
	first = pieces[0]
	rest = pieces[1:]

	if rest:
		acc = gen_pallets(rest, pallet_len)
	else:
		return [[first]]

	new_acc = acc[:]

	for pallet in acc:
		if sum(pallet + [first]) < pallet_len:
			new_acc.append(pallet + [first]) # new el to the end of pallet
		temp = pallet[:]
		for i in range(len(pallet)):
			new_combi = temp.insert(i,first) # new pallet variant
			if new_combi and sum(new_combi) < pallet_len:
				new_acc.append(new_combi)
	new_acc.append([first]) # new el as new pallet
	return new_acc

def delete_same_combis(combis):
	"""
	takes list of combis and delete the same 
	same are in combis because many elemets of the same length
	returns list of distinct conbis
	"""
	acc = []
	
	temp = combis.pop(0)
	while temp:
		if temp not in combis:
			acc.append(temp)

		if combis:
			temp = combis.pop(0)
		else:
			break

	return acc

def gen_cuts(pallets):
	"""
	takes list of lists
	generates combis for cuts in repect to num of specified elements
	returns list of lists of pallet(list of elements)
	"""
	first = pallets[0]
	rest = pallets[1:]
	# print 'First:', first
	# print "Rest:", rest

	if rest:
		cuts = gen_cuts(rest)
	else:
		return {0 : first}

	acc = cuts.copy()
	for pallet in cuts.values():
		new_cut = []
		new_cut.append(pallet)
		new_cut.append(first)
		acc[len(acc)] = new_cut
	acc[len(acc)] = first
	return acc

	# acc = cuts[:]
	# new_cut_acc = []
	# print
	# print "Cuts:", cuts
	# for cut in cuts:
	# 	new_cut = []
	# 	new_cut.append(cut)
	# 	new_cut.append(first)
	# 	new_cut_acc.append(new_cut)
	# 	print "new_cut:", new_cut
	# 	print "new_cut_acc:", new_cut_acc
	# 	print
	
	# 	for new_cut in new_cut_acc:
	# 		acc.append(new_cut)
	# print "acc:", acc
	# return acc



def nested_sum(nested_list):
	'''
	sums elements in nested list
	elements must be numbers
	'''
	total = 0

	for elem in nested_list:
		if isinstance(elem, list):
			total += nested_sum(elem)
		else:
			total += elem

	return total


elem = get_pieces_from_file('elements.txt',';')
sum_length = sum(elem)

print "All elements:", elem
print 'Total length: ', sum_length

allcombis = gen_pallets(elem,6)

# print '-'*40
# print "All combis:", allcombis
# print
# print "Len:", len(allcombis)
# print '-'*40 + '\n'

distinc_combis = delete_same_combis(allcombis)

print '-'*40
print 'Distinct combis:',distinc_combis
print
print "Len:", len(distinc_combis)
print '-'*40 + '\n'

cuts = gen_cuts(distinc_combis)
output = open('out.txt','w')
for cut in cuts:
	output.write(str(cut) + '\n')
output.close()

# print '-'*40
# print "Len:", len(cuts)
print cuts
# for cut in cuts:
# 	print cut
# print

# print '-'*40 + '\n'


