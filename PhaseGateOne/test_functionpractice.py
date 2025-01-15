import unittest
import functionpractice

class TestIntegerFunctions(unittest.TestCase):


	def test_that_integer_function_return_invalid_data_with_invalid_input(self):
		actual = functionpractice.get_integer('a')
		result = 'invalid data'
		self.assertEqual(actual, result)

	def test_that_integer_function_return_positive_value(self):
		actual = functionpractice.get_integer(9)
		result = 14
		self.assertEqual(actual , result)


	def test_that_takes_integer_function_and_subtract(self):
		actual = functionpractice.get_integer(9)
		result = 14
		self.assertEqual(actual , result)


	def test_that_takes_integer_function_and_multiply(self):
		actual = functionpractice.get_integer(7)
		result = 49
		self.assertEqual(actual , result)

