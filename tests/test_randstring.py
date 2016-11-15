import unittest
import sys
sys.path.append('../src')
import randstring

class TestRandstring(unittest.TestCase):
	def test_gen_word_default_length(self):
		result = randstring.gen_word()

		self.assertGreaterEqual(len(result), 4)
		self.assertLessEqual(len(result), 20)


	def test_gen_word_custom_length(self):
		desired_length = 12

		result = randstring.gen_word(desired_length, desired_length)

		self.assertEqual(len(result), desired_length)


	def test_gen_word_alternation(self):
		result = randstring.gen_word()

		if(result[0] in randstring.VOWELS):
			 odd_letters = randstring.VOWELS;
			 even_letters = randstring.CONSONANTS
		else:
			odd_letters = randstring.CONSONANTS
			even_letters = randstring.VOWELS

		for i in range(len(result)):
			if i % 2 == 1:
				self.assertIn(result[i], even_letters)
			elif i % 2 == 0:
				self.assertIn(result[i], odd_letters)


if(__name__ == '__main__'):
	unittest.main()
