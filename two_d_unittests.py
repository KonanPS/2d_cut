import unittest

from two_d_cut import nested_sum

class TestNestedSum(unittest.TestCase):
	def test_nested_sum(self):
		self.assertEqual(nested_sum([1,2,[3,4,5],[6,7,[8,10]],9]),55)

if __name__ == '__main__':
	unittest.main()