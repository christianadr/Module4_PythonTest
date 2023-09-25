"""
    Name: Christian Del Rosario
    Course/Section: CPE 028 - CPE41S2
    Date: September 25, 2023
    Activity Programming 4.1 - Python Test
"""

import unittest

def multiply(x,y):
    return x*y

class TestMultiply(unittest.TestCase):

    def test(self):
        self.assertEqual(multiply(4,2), 8)
    

if __name__ == '__main__':
    unittest.main()