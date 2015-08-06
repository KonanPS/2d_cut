import unittest

from two_d_cut import nested_sum, gen_pallets

class TestNestedSum(unittest.TestCase):
	def test_nested_sum(self):
		self.assertEqual(nested_sum([1,2,[3,4,5],[6,7,[8,10]],9]),55)
		self.assertEqual(nested_sum([1,2,[3,4,5],[6,7,[8,10,[]]],9]),55)
		self.assertEqual(nested_sum([1,2,[3,4,5,[]],[6,7,[8,10]],9,[]]),55)

class TestGenPallets(unittest.TestCase):
	def test_gen_pallets(self):
		self.assertEqual(gen_pallets([1,2,3],8), [[3],[2],[2,3],[3,2],[1],[1,3],[3,1],[1,2],[2,1],[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]) #all combis pallet_len == 8 > than any sum
		self.assertEqual(gen_pallets([1,2,3],4), [[3],[2],[1],[1,3],[3,1],[1,2],[2,1]]) #[3,2] is greater than pallet_len == 4




if __name__ == '__main__':
	unittest.main()