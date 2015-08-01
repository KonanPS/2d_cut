
def get_pieces_from_file(filename, separator):
	"""
	opens file with pieces in format
	length; number

	returns list with all elements
	"""	
	elements = open(filename)

	pieces = []
	pieces_dict = {}

	line = elements.readline()
	while line:
		temp = line.split(separator)
		length = float(temp[0])
		num = int(temp[1])
		pieces_dict[length] = num
		for _ind in range(num):
			pieces.append(length)

		line = elements.readline()

	elements.close()

	return pieces, pieces_dict

def gen_pallets(pieces, pallet_len):
	"""
	takes list of all pieces and
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
	# print 'new_acc: ', new_acc
	new_acc.append([first])

	for pallet in acc:
		# print 'pallet in acc: ', pallet
		new_pallet = pallet[:]
		new_pallet.append(first)
		if sum(new_pallet) < pallet_len:
			new_acc.append(new_pallet)
			
			for i in range(len(pallet) + 1):
				temp = pallet[:]
				# print 'temp before insert', temp
				temp.insert(i,first)
				# print 'temp after insert: ', temp
				new_acc.append(temp)

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

def gen_cuts(pallets, total_len):
	"""
	takes list of lists
	generates combis for cuts in repect to num of specified elements
	returns list of lists of pallet(list of elements)
	"""
	first = pallets[0]
	rest = pallets[1:]

	if rest:
		cuts = gen_cuts(rest, total_len)
	else:
		return {0 : pallets}
	# print 'cuts: ', cuts
	# print 'cuts_values: ', cuts.values()
	acc = cuts.copy()
	for pallets in cuts.values():
		# print 'pallet in cuts.values', pallets
		for pallet in pallets:
			new_cut = []
			new_cut.append(pallet)
			new_cut.append(first)
			if nested_sum(new_cut) == total_len:
					acc[len(acc)] = new_cut
	acc[len(acc)] = [first]
	
	return acc

def best_cut(cuts, PALLET_LEN):
	"""
	takes dict with possible cuts
	returns best cut
	"""
	result = {}
	# key = 0
	# print '\ncuts.values():', len(cuts.values())
	for item in cuts.items():
		cut = item[1]
		print 'cut:', cut
		residues = 0
		for pallet in cut:
			residues += PALLET_LEN - sum(pallet)
		result[item[0]] = residues # key is the key in cuts dict
		# key += 1
	return result

def is_contains_specified_elems(cut,pieces_dict):
	"""
	check if cut contains exectlly specified pieses
	"""
	cut_details = {}
	for pallet in cut:
		for elem in pallet:
			# print pallet, elem
			if elem in cut_details:
				cut_details[elem] += 1
			else:
				cut_details[elem] = 1
	# print cut_details
	# print cut_details == pieces_dict
	if cut_details == pieces_dict:
		return True
	else:
		return False

def filter_cuts_by_num_elem(cuts,pieces_dict):
	"""
	leaves cuts that uses specified num of pieces
	"""
	for key in cuts.keys():
		if not is_contains_specified_elems(cuts[key],pieces_dict):
			del cuts[key]

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


elem, pieces_dict = get_pieces_from_file('elements.txt',';')
sum_length = sum(elem)

print "All elements:", elem
print "pieces_dict:", pieces_dict
print 'Total length: ', sum_length

allcombis = gen_pallets(elem,6)

# print '-'*40
# print "All combis:", allcombis
# print
# print "Len:", len(allcombis)
# print '-'*40 + '\n'

distinc_combis = delete_same_combis(allcombis)

# print '-'*40
# print 'Distinct combis:',distinc_combis
# print
# print "Len:", len(distinc_combis)
# print '-'*40 + '\n'

cuts = gen_cuts(distinc_combis, sum_length)
# print 'Cuts before filter:', cuts
# print

filter_cuts_by_num_elem(cuts, pieces_dict)
print "Filtered Cuts:", cuts
print

print 'best_cut:', best_cut(cuts,6)
# output = open('out.txt','w')
# for cut in cuts:
# 	output.write(str(cut) + '\n')
# output.close()

# print '-'*40
# print "Len:", len(cuts)

# for cut in cuts:
# 	print cut
# print

# print '-'*40 + '\n'


