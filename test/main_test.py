import unittest
from main import *


class TestAddNum(unittest.TestCase):
    def test_if_addNumber_return_addittion_of_two_numbers(self):
        test_add = addNumber(7,3)
       
        self.assertEqual(test_add, 10)
        
    def test_if_addNumber_returns_error_when_it_is_not_a_number(self):
        test_add = addNumber(9,"boss")
        # print (test_add )
        self.assertIn(test_add, "one of your inputs is not a number",msg="this is not a number could not be found at all in the database")
        
        
                
if __name__ == '__main__':
    unittest.main()        