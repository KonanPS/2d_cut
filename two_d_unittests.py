import unittest

from two_d_cut import gen_pallets, delete_same_combis

class TestBaseFuncs(unittest.TestCase):

	pass
	# def test_gen_pallets(self):
	# 	self.assertEqual(gen_pallets([1,2,3],8), [[3],[2],[2,3],[3,2],[1],[1,3],[3,1],[1,2],[2,1],[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]) #all combis pallet_len == 8 > than any sum
	# 	self.assertEqual(gen_pallets([1,2,3],4), [[3],[2],[1],[1,3],[3,1],[1,2],[2,1]]) #[3,2] is greater than pallet_len == 4

	# def test_delete_same_combis(self):
	# 	self.assertEqual(delete_same_combis([[1,2],[1,2],[1,2]]), [[1,2]])
	# 	self.assertEqual(delete_same_combis([[1,2],[1,3,5],[1,2]]), [[1,3,5],[1,2]])
	# 	self.assertEqual(delete_same_combis([1,2,3,1,4,1,6,2,7]), [3,4,1,6,2,7])

if __name__ == '__main__':
	unittest.main()