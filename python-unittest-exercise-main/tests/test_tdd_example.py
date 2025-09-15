import unittest
from src.tdd_example import TDDExample
 
class TestTDDExample(unittest.TestCase):
 
    def setUp(self):
        self.tdd = TDDExample()
 
    def test_reverse_string(self):
        self.assertEqual(self.tdd.reverse_string("foobar"), "raboof")
        self.assertEqual(self.tdd.reverse_string(""), "")
        self.assertIsNone(self.tdd.reverse_string(None))
 
    def test_find_longest_word(self):
        sentence = '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        '''
        self.assertEqual(self.tdd.find_longest_word(sentence), "consectetur")
        self.assertEqual(self.tdd.find_longest_word(""), "")
 
    def test_reverse_list(self):
        self.assertEqual(self.tdd.reverse_list([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(self.tdd.reverse_list([]), [])
 
    def test_count_digits(self):
        self.assertEqual(self.tdd.count_digits([1, 1, 1, 2, 3], 1), 3)
        self.assertEqual(self.tdd.count_digits([], 1), 0)
 
if __name__ == "__main__":
    unittest.main()