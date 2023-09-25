"""
    Name: Christian Del Rosario
    Course/Section: CPE 028 - CPE41S2
    Date: September 25, 2023
    Activity Programming 4.1 - Python Test
"""

import unittest

def fun(x):
    return x+1

class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(fun(5), 6)
    

if __name__ == '__main__':
    unittest.main()