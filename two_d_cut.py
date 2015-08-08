
def get_data_from_file(filename, separator):
	"""
	opens file with pieces in format
	length; number

	returns list with all elements
	"""	
	elements = open(filename)

	pieces_list = []
	pieces_dict = {}

	PALLET_LEN = int(elements.readline()) #first line is pallet length

	line = elements.readline()
	while line:
		temp = line.split(separator)
		length = float(temp[0])
		num = int(temp[1])
		pieces_dict[length] = num

		for _ind in range(num):
			pieces_list.append(length)

		line = elements.readline()

	elements.close()

	return pieces_list, pieces_dict, PALLET_LEN

def gen_pallets(pieces):
	"""
	takes list of all pieces and
	generates all possible combinations of different length
	returns list of conbis (list)
	"""
	first = pieces[0]
	rest = pieces[1:]

	if rest:
		acc = gen_pallets(rest)
	else:
		return [[first]]

	new_acc = acc[:]
	new_acc.append([first])

	for pallet in acc:
		if sum(pallet) + first <= PALLET_LEN:
			for i in range(len(pallet) + 1):
				temp = pallet[:]
				temp.insert(i,first)
				if temp not in new_acc: #filter same pallets because of same elements
					new_acc.append(temp)

	return new_acc

def delete_same_combis(combis):
	"""
	takes list of combis and delete the same 
	same are in combis because many elemets of the same length
	returns list of distinct combis
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

def delete_short_cuts(combis, MAX_ELEMENT_LENGTH):
	"""
	deletes combi that has residues more than max length of element
	"""
	acc = []
	for combi in combis:
		if (PALLET_LEN - sum(combi)) <= MAX_ELEMENT_LENGTH:
			acc.append(combi)

	combis = acc

	return combis

# def gen_cuts(pallets_list, MAX_PALLEN_NUM):
# 	"""
# 	takes list of lists
# 	generates combis for cuts in repect to num of specified elements
# 	returns dict pallet_id : pallet (list of elements) 
# 	pallet_id starts from 0
# 	pallets_list is list of distinct combi of elements within pallet length [[1],[2],[3],[1,2],[1,3],[2,1],[2,3],[3,1],[3,2],[1,2,3],...]
# 	"""
# 	first = pallets_list[0]
# 	rest = pallets_list[1:]

# 	if rest:
# 		cuts = gen_cuts(rest, MAX_PALLEN_NUM)
# 	else:
# 		return pallets_list # [[[1,2,3]]]

# 	acc = cuts[:]

# 	for cut in cuts: #list of pallets combinations. pallets cut on elements
# 		new_cut = cut[:]
# 		new_cut.append(first)
# 		if len(new_cut) <= MAX_PALLEN_NUM:
# 			acc.append(new_cut) # add element to dict with next id (incremented from num of id in dict already)
		
# 	acc.append([first]) 
# 	print len(acc)
# 	# print acc
# 	return acc

# def best_cut(cuts, PALLET_LEN):
# 	"""
# 	takes dict with possible cuts
# 	returns best cut
# 	"""
# 	result = {}
# 	# key = 0
# 	# print '\ncuts.values():', len(cuts.values())
# 	for item in cuts.items():
# 		cut = item[1]
# 		# print 'cut:', cut
# 		residues = 0
# 		for pallet in cut:
# 			residues += PALLET_LEN - sum(pallet)
# 		result[item[0]] = residues # key is the key in cuts dict
# 		# key += 1
# 	return result

# def is_contains_specified_elems(cut,pieces_dict):
# 	"""
# 	check if cut contains exectlly specified pieses
# 	"""
# 	cut_details = {}
# 	for pallet in cut:
# 		for elem in pallet:
# 			# print pallet, elem
# 			if elem in cut_details:
# 				cut_details[elem] += 1
# 			else:
# 				cut_details[elem] = 1
# 	# print cut_details
# 	# print cut_details == pieces_dict
# 	if cut_details == pieces_dict:
# 		return True
# 	else:
# 		return False

# def filter_cuts_by_num_elem(cuts,pieces_dict):
# 	"""
# 	leaves cuts that uses specified num of pieces
# 	"""
# 	for key in cuts.keys():
# 		if not is_contains_specified_elems(cuts[key],pieces_dict):
# 			del cuts[key]

# def nested_sum(nested_list):
# 	'''
# 	sums elements in nested list
# 	elements must be numbers
# 	'''
# 	total = 0

# 	for elem in nested_list:
# 		if isinstance(elem, list):
# 			total += nested_sum(elem)
# 		else:
# 			total += elem

# 	return total

# def get_cut_with_min_residue(pallets_list):
# 	"""
# 	returns palet with min residue
# 	"""
# 	min_resudue = PALLET_LEN

# 	for pallet in pallets_list:
# 		if  PALLET_LEN - sum(pallet) < min_resudue:
# 			min_cut = pallet
# 			min_resudue = PALLET_LEN - sum(pallet)
# 	print min_resudue
# 	return min_cut

if __name__ == '__main__':
	
#FIXME delete pallets with the same num of elements
	global PALLET_LEN

	elem, pieces_dict, PALLET_LEN = get_data_from_file('elements.txt',';') # elem, pieces_dict and PALLET_LEN
	sum_length = sum(elem)
	
	MAX_PALLEN_NUM = int(sum_length / PALLET_LEN) + 1
	MAX_ELEMENT_LENGTH = max(elem)

	print "PALLET_LEN:", PALLET_LEN
	print "All elements:", elem
	print "MAX_ELEMENT_LENGTH:", MAX_ELEMENT_LENGTH
	print "pieces_dict:", pieces_dict
	print 'Total length: ', sum_length

	print 'Step 1. gen_pallets...starts'
	allcombis = gen_pallets(elem)
	print 'Step 1. gen_pallets...Done'
	# print '-'*40
	# print "All combis:", allcombis
	# print
	# print "Len:", len(allcombis)
	# print '-'*40 + '\n'

	print 'Step 2. distinc_combis...starts'
	distinc_combis = delete_same_combis(allcombis)
	print 'Step 2. distinc_combis...Done'
	print "Len:", len(distinc_combis)
	print '-'*40
	# print 'Distinct combis:',distinc_combis[:26]
	print
	# print "Len:", len(distinc_combis)
	# print '-'*40 + '\n'

	print 'Step 2.1 delete_short_cuts...starts'
	distinc_combis = delete_short_cuts(distinc_combis, MAX_ELEMENT_LENGTH)
	print 'Step 2.1 delete_short_cuts...Done'
	print "Len:", len(distinc_combis)
	# print "Slice distinc_combis:", distinc_combis[1000:1011]
	print '-'*40
	print

	print 'Step 3. geting cuts.... starts'
	# print "cut_with_min_residue:", get_cut_with_min_residue(distinc_combis, PALLET_LEN)

	distinc_combis_sorted = sorted(distinc_combis, key=lambda pallet: PALLET_LEN - sum(pallet))
	# print "Sorted with lambda:", distinc_combis_sorted[0]
	# print "residues =", PALLET_LEN - sum(distinc_combis_sorted[0])

	temp_pieces_dict = pieces_dict.copy()
	i = 0
	total_residue = 0
	while sum(temp_pieces_dict.values()):
		
		combi_can_be_cut = True

		elem_to_cut = {}
		for elem in distinc_combis_sorted[i]:
			if elem in elem_to_cut:
				elem_to_cut[elem] += 1
			else:
				elem_to_cut[elem] = 1

		for key, val in elem_to_cut.items():
			if temp_pieces_dict[key] >= val:
				continue
			else:
				combi_can_be_cut = False
				break

		if combi_can_be_cut:
			residue = PALLET_LEN - sum(distinc_combis_sorted[i])
			print i, distinc_combis_sorted[i], 'residue=', residue
			total_residue += residue
			for key, val in elem_to_cut.items():
				temp_pieces_dict[key] -= val

		else: #try the same combi because it has min residue
			i += 1 
	print total_residue


	# print 'Step 3. gen_cuts...starts'
	# cuts = gen_cuts(distinc_combis, MAX_PALLEN_NUM)
	# print 'Step 3. gen_cuts...Done'
	# print 'Cuts before filter:', cuts
	# print
	# print 'Cuts: ',cuts
	# print

	# print 'Step 4. filter_cuts_by_num_elem...starts'
	# filter_cuts_by_num_elem(cuts, pieces_dict)
	# print 'Step 4. filter_cuts_by_num_elem...Done'
	# print "Filtered Cuts:", cuts
	# print

	# print 'best_cut:', best_cut(cuts, PALLET_LEN)
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


