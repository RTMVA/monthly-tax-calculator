import unittest
from logic_class import Employee

class tester(unittest.TestCase):

    def test_my(self):

        cases = [3,4,2,1]

        for num in cases:
            with self.subTest(num=num):
                self.assertTrue(num > 0)

unittest.main()